from flask import render_template, request, redirect, session, flash
import requests
from utils.handler_api import server_data
from utils.anomaly_detection import AnomalyDetection
from models.dx1_af_model import DX1AFApiModel
from utils.handler_api import compressors
import pandas as pd
from datetime import datetime

class CompressorAfController:
    def index(self, id):
        dx1_model = DX1AFApiModel(api_url=compressors['dx1af1']) if id == 1 else DX1AFApiModel(api_url=compressors['dx1af2'])
        df_test, start, end = None, None, None
        if request.method == 'POST':
            start = request.form.get('start')
            end = request.form.get('end')
            df_test = dx1_model.fetch_data(start, end)
        else:
            df_test = dx1_model.fetch_data_now()

        data = None

        if df_test.empty:
            data = {
                'date': datetime.today().strftime('%Y-%m-%d'),
                'columns': None,
                'data': None,
                'anomalies': None,
                'plots': None,
                'attributes': None,
                'causes_recommendations': None
            }
        else:
            anomalyDetection = AnomalyDetection()
            train_path = 'static/datasets/train-data-prod.xlsx'
            df_train = anomalyDetection.load_data_train(train_path)
            
            drop_timestamps = df_train.drop(columns=['timestamps'])
            data_train_features = drop_timestamps.drop_duplicates()
            data_test_features = df_test.drop(columns=['timestamps'])
            model, train_anomaly_scores = anomalyDetection.train_isolation_forest(data_train_features)

            # Prediksi anomali pada data test
            predictions = model.predict(data_test_features)
            anomaly_scores = model.decision_function(data_test_features)

            df_test['anomali'] = predictions
            
            parameters = anomalyDetection.parameters_scalar(model, data_train_features, data_test_features, df_test)
            plot_parameters = anomalyDetection.plot_parameters_scalar(parameters['features'], parameters['mean_shap_value'], parameters['scalar'])

            root_cause_path = 'static/datasets/root-cause-af.xlsm'
            causes_recommendations = anomalyDetection.get_causes_and_recommendations(root_cause=root_cause_path, shap_df_anomali=parameters)

            data = {
                'date': datetime.today().strftime('%Y-%m-%d'),
                'columns': df_test.columns,
                'data': df_test.to_records(index=False),
                'anomalies': df_test[df_test['anomali'] == -1].to_records(index=False),
                'plots': plot_parameters,
                'attributes': parameters.to_records(index=False),
                'causes_recommendations': causes_recommendations
            }

        return render_template('compressors/index.html', data=data)