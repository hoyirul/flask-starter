from flask import render_template, request, redirect, session, flash
import requests
from utils.handler_api import base_url
from utils.anomaly_detection import AnomalyDetection
from models.dx1_af1_model import DX1AF1ApiModel

class CompressorAfController:
    def index(self):
        anomalyDetection = AnomalyDetection()
        train_path = 'static/datasets/train-data-prod.xlsx'
        df_train = anomalyDetection.load_data_train(train_path)
        
        dx1_model = DX1AF1ApiModel(api_url=base_url)
        df_test = dx1_model.fetch_data_now()
        
        drop_timestamps = df_train.drop(columns=['timestamps'])
        data_train_features = drop_timestamps.drop_duplicates()
        data_test_features = df_test.drop(columns=['timestamps'])
        model, train_anomaly_scores = anomalyDetection.train_isolation_forest(data_train_features)

        # Prediksi anomali pada data test
        predictions = model.predict(data_test_features)
        anomaly_scores = model.decision_function(data_test_features)

        df_test['anomali'] = predictions

        print(df_test)

        return render_template('compressors/index.html')