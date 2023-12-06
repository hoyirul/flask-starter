import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import shap
from sklearn.preprocessing import MinMaxScaler

class AnomalyDetection:
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

    def get_causes_and_recommendations(self, root_cause, feature):
        df_rc = pd.read_excel(root_cause, sheet_name=f'{feature}')
        causes = df_rc.loc[df_rc['penyebab'].notnull(), 'penyebab'].tolist()
        recommendations = df_rc.loc[df_rc['perbaikan'].notnull(), 'perbaikan'].tolist()
        return causes, recommendations