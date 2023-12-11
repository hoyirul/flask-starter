import requests
import pandas as pd
import datetime

now = datetime.datetime.now()  # Mendapatkan tanggal dan jam saat ini

class DX1AFApiModel:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self, start_date, end_date):
        try:
            response = requests.get(self.api_url, params={"start": start_date, "end": end_date})
            if response.status_code == 200:
                data = response.json()
                df = pd.DataFrame(data)  # asumsikan API mengembalikan data dalam format DataFrame
                # print(df)
                return df
            else:
                print(f"Error: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error: {str(e)}")
            return None

    def fetch_data_now(self):
        try:
            # Jika kamu ingin menggunakan tanggal saat ini, atur start_date dan end_date sesuai kebutuhan
            start_date = datetime.datetime.now().strftime('%Y-%m-%d')
            end_date = datetime.datetime.now().strftime('%Y-%m-%d')
            response = requests.get(self.api_url, params={"start": start_date, "end": end_date})
            if response.status_code == 200:
                data = response.json()
                df = pd.DataFrame(data)  # asumsikan API mengembalikan data dalam format DataFrame
                # print(df)
                return df
            else:
                print(f"Error: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error: {str(e)}")
            return None
