from dotenv import load_dotenv
import os

# Muat variabel lingkungan dari file .env
load_dotenv()

class HandlerApi:
  def api_url(self):
    api_server = None
    if os.getenv("APP_DEBUG") == 'development':
      # api_server = 'http://192.168.9.47:3270'
      api_server = 'http://192.168.9.47:3100'
    else:
      api_server = 'http://localhost:3100'
    
    return api_server

base_url = f'{HandlerApi().api_url()}'
endpoint_login = f'{HandlerApi().api_url()}/users/login'