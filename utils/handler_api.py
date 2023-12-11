from dotenv import load_dotenv
import os

# Muat variabel lingkungan dari file .env
load_dotenv()

server_login = 'http://192.168.9.47:3270'
# server_data = 'http://192.168.9.47:3100'
server_data = 'http://localhost:3100'

endpoint_login = f'{server_login}/users/login'

compressors = {
  'dx1af1': f'{server_data}/ml/dx1af1',
  'dx1af2': f'{server_data}/ml/dx1af2',
}