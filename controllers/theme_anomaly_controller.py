from flask import render_template, request, redirect, session, flash
import requests
from utils.handler_api import server_data
from utils.anomaly_detection import AnomalyDetection
from models.dx1_af1_model import DX1AF1ApiModel
import pandas as pd
from datetime import datetime
import os

class ThemeAnomalyController:
    def index(self):
        dx1_model = DX1AF1ApiModel(api_url=server_data)
        
        train_file_path, test_file_path = '', ''

        if request.method == 'POST':
            train_file = request.files['train_file']
            test_file = request.files['test_file']
            
            train_file_path = os.path.join('static/uploads', train_file.filename)
            test_file_path = os.path.join('static/uploads', test_file.filename)
            train_file.save(train_file_path)
            test_file.save(test_file_path)

        anomalyDetection = AnomalyDetection()

        # Load data from default paths if uploaded files don't exist
        if not train_file_path or not test_file_path:
            train_file_path = 'static/datasets/format_train.xlsx'
            test_file_path = 'static/datasets/format_test.xlsx'
        
        df_train, df_test = anomalyDetection.load_data_upload(train_file_path, test_file_path)

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

        data = {
            'date': datetime.today().strftime('%Y-%m-%d'),
            'columns': df_test.columns,
            'data': df_test.to_records(index=False),
            'anomalies': df_test[df_test['anomali'] == -1].to_records(index=False),
            'plots': plot_parameters,
            'attributes': parameters.to_records(index=False)
        }

        return render_template('theme-anomalies/index.html', data=data)