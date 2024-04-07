import sqlite3
import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    DB_CONNECTION = os.getenv("DB_CONNECTION")
    DB_DATABASE = os.getenv("DB_DATABASE")

    def __init__(self):
        if self.DB_CONNECTION == 'sqlite':
            self.connection = sqlite3.connect(self.DB_DATABASE, check_same_thread=False)
            self.connection.row_factory = sqlite3.Row
        elif self.DB_CONNECTION == 'mysql':
            # Sesuaikan dengan konfigurasi MySQL Anda
            DB_HOST = os.getenv("DB_HOST")
            DB_PORT = os.getenv("DB_PORT")
            DB_USERNAME = os.getenv("DB_USERNAME")
            DB_PASSWORD = os.getenv("DB_PASSWORD")
            DB_DATABASE = os.getenv("DB_DATABASE")
            self.connection = pymysql.connect(
                host=DB_HOST,
                port=int(DB_PORT),
                user=DB_USERNAME,
                password=DB_PASSWORD,
                database=DB_DATABASE,
                cursorclass=pymysql.cursors.DictCursor
            )
        else:
            raise ValueError("Unsupported database connection:", self.DB_CONNECTION)

    def check_connection(self):
        if self.connection:
            print("Connection success")
        else:
            print("Connection failed")
        self.connection.close()

    def get_connection(self):
        return self.connection

    def close_connection(self):
        self.connection.close()