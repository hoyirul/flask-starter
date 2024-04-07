
from config.config import Config

class UserSeeder:
    def __init__(self):
        self.connection = Config().get_connection()
        self.cursor = self.connection.cursor()
        self.table = 'users'
    
    def run(self):
        data = { 
            'id': 1,
         }
        query = f"INSERT INTO {self.table} ({', '.join(data.keys())}) VALUES ({', '.join(data.values())})"
        self.cursor.execute(query)
        self.connection.commit()
        print(f"Seeder {self.table} created")
    
    def __del__(self):
        Config().close_connection()
