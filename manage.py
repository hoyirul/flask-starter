from flask import Flask
from routes.route import main  # Import blueprint yang telah Anda buat
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Muat variabel lingkungan dari file .env
load_dotenv()

# Registrasi blueprint
app.register_blueprint(main)

if __name__ == '__main__':
    # Mendapatkan nilai dari variabel lingkungan
    app_name = os.getenv("APP_NAME")
    debug_mode = os.getenv("APP_DEBUG")
    local_host = os.getenv("APP_LOCAL")
    host_ip = os.getenv("APP_HOST")
    app_port = os.getenv("APP_PORT")  # Menambah variabel untuk port

    # Menentukan host dan port berdasarkan mode (development/production)
    if debug_mode == 'development':
        host = local_host
        port = 5000 if app_port is None else int(app_port)
    else:
        host = host_ip
        port = 80 if app_port is None else int(app_port)

    app.run(debug=True if debug_mode == 'development' else False, host=host)
