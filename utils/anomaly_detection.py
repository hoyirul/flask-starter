import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import shap
from sklearn.preprocessing import MinMaxScaler
import plotly.graph_objs as go

class AnomalyDetection:
    def load_data_upload(self, train_path, test_path):
        df_train = pd.read_excel(train_path)
        df_test = pd.read_excel(test_path)
        return df_train, df_test

    def load_data_train(self, train_path):
        df_train = pd.read_excel(train_path)
        return df_train
    
    def load_data_test(self, start, end):
        dx1_model = DX1AF1ApiModel(api_url=api_url)
        df_test = dx1_model.fetch_data(start, end)
        return df_test

    def train_isolation_forest(self, data_train_features):
      contamination = 0.04
      n_estimators = 100
      max_samples = 100
      bootstrap = True
      max_features = 1.0
      random_state = 30

      model = IsolationForest(
          n_estimators=n_estimators,
          max_samples=max_samples,
          contamination=contamination,
          bootstrap=bootstrap,
          random_state=random_state
      )

      model.fit(data_train_features)
      train_anomaly_scores = model.decision_function(data_train_features)

      return model, train_anomaly_scores    

    def parameters_scalar(self, model, data_train_features, data_test_features, df_test):
        data_test_anomali = data_test_features[df_test['anomali'] == -1]

        if not data_test_anomali.empty:
            # Mendapatkan SHAP values untuk data test yang merupakan anomali
            explainer = shap.Explainer(model, data_train_features)
            shap_values_anomali = explainer.shap_values(data_test_anomali)
            scaler = MinMaxScaler(feature_range=(0, 1))

            shap_df_anomali = pd.DataFrame(list(zip(data_train_features.columns, np.mean(np.abs(shap_values_anomali), axis=0))),
                                            columns=['features', 'mean_shap_value'])
            # Menormalisasi kolom Mean SHAP Value ke rentang 0-1
            shap_df_anomali['scalar'] = scaler.fit_transform(shap_df_anomali[['mean_shap_value']])
            shap_df_anomali = shap_df_anomali.sort_values('scalar', ascending=False)
            
            return shap_df_anomali
        else:
            # Tidak ada data yang terdeteksi sebagai anomali, atur nilai default atau kembalikan pesan
            return pd.DataFrame(columns=['features', 'mean_shap_value', 'scalar'])

    def plot_parameters_scalar(self, features, mean_shap_value, scalar):
        # Menggunakan data yang telah disediakan
        data = {
            'features': features,
            'mean_shap_value': mean_shap_value,
            'scalar': scalar,
        }

        bar_colors = ['rgba(255, 99, 71, {})'.format(scalar) if scalar > 0.75 else 'rgba(54, 162, 235, 0.9)'.format(scalar) for scalar in data['scalar']]

        trace = go.Bar(
            x=data['features'],
            y=data['mean_shap_value'],
            marker=dict(color=bar_colors),
        )

        layout = go.Layout(
            title='Chart Atribut yang Berpengaruh Terhadap Anomali',
            xaxis=dict(title='Features'),
            yaxis=dict(title='Mean Shap Value')
        )

        fig = go.Figure(data=[trace], layout=layout)

        return fig.to_html(full_html=False, include_plotlyjs=False)

    def get_causes_and_recommendations(self, root_cause, shap_df_anomali):
        results = []
        for index, row in shap_df_anomali.iterrows():
            if row['scalar'] > 0.75:
                feature = row['features']
                causes, recommendations = self.parse_root_cause(root_cause, feature)
                data = {'Feature': feature, 'Causes': causes, 'Recommendations': recommendations}
                results.append(data)
        return results

    def parse_root_cause(self, root_cause, feature):
        df_rc = pd.read_excel(root_cause, sheet_name=f'{feature}')
        causes = df_rc.loc[df_rc['penyebab'].notnull(), 'penyebab'].tolist()
        recommendations = df_rc.loc[df_rc['perbaikan'].notnull(), 'perbaikan'].tolist()
        return causes, recommendations