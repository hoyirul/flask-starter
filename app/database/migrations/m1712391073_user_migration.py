
from config.config import Config

class UserMigration:
    def __init__(self):
        self.connection = Config().get_connection()
        self.cursor = self.connection.cursor()
        self.table = 'users'
    
    def up(self):
        query = f'''CREATE TABLE {self.table} (
            id VARCHAR(10) PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            password VARCHAR(255) NOT NULL,
            ip_address VARCHAR(20) NOT NULL,
            address TEXT NOT NULL,
            is_active BOOLEAN NOT NULL,
            last_logged_in TIMESTAMP NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )'''
        self.cursor.execute(query)
        self.connection.commit()
        print(f"Table {self.table} created")
    
    def down(self):
        query = f"DROP TABLE {self.table}"
        self.cursor.execute(query)
        self.connection.commit()
        print(f"Table {self.table} dropped")
    
    def __del__(self):
        Config().close_connection()
