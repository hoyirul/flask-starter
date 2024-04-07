
from config.config import Config

class UserModel:
    def __init__(self):
        self.connection = Config().get_connection()
        self.cursor = self.connection.cursor()
        self.table = 'users'
        self.column_names = []
    
    def findAll(self, data=None):
        column = ', '.join(data) if data else '*'
        query = f"SELECT {column} FROM {self.table}"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def findById(self, id, data):
        column = ', '.join(data) if data else '*'
        query = f"SELECT {column} FROM {self.table} WHERE id = {id}"
        self.cursor.execute(query)
        return self.cursor.fetchone()
    
    def create(self, data):
        if 'csrf_token' in data:
            del data['csrf_token']  # Hapus CSRF token dari data
        # Membuat bagian VALUES untuk query INSERT
        values = []
        for value in data.values():
            # Memeriksa apakah nilai adalah string
            if isinstance(value, str):
                # Jika nilai adalah string, tambahkan tanda kutip di sekitarnya
                values.append(f"'{value}'")
            else:
                # Jika nilai adalah number, biarkan tanpa tanda kutip
                values.append(str(value))

        # Menggabungkan nilai-nilai menjadi string dengan koma di antaranya
        values_string = ', '.join(values)
        query = f"INSERT INTO {self.table} ({', '.join(data.keys())}) VALUES ({values_string})"
        self.cursor.execute(query)
        self.connection.commit()
        return self.cursor.lastrowid
    
    def update(self, id, data):
        query = f"UPDATE {self.table} SET {', '.join([f'{key} = {value}' for key, value in data.items()])} WHERE id = {id}"
        self.cursor.execute(query)
        self.connection.commit()
        return self.cursor.rowcount
    
    def delete(self, id):
        query = f"DELETE FROM {self.table} WHERE id = {id}"
        self.cursor.execute(query)
        self.connection.commit()
        return self.cursor.rowcount
    
    def __del__(self):
        Config().close_connection()
