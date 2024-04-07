from flask import Flask
from app.routes.web import web_routes
from app.routes.api import api_routes
from dotenv import load_dotenv
import os
from app.handlers.error_handler import ErrorHandler as Err
from flask_wtf import CSRFProtect
from flask_cors import CORS

# Inisialisasi Flask
app = Flask(__name__, template_folder='app/views', static_folder='public')
csrf = CSRFProtect(app)
CORS(app, resources={r"/*": {"origins": "*"}}, methods=["GET", "POST", "PUT", "DELETE"])

@app.route('/public/<path:filename>')
def public(filename):
    return send_from_directory(app.static_folder, filename)

# Registrasi handler error
err = Err()
@app.errorhandler(404)
def not_found_error(error):
    return err.not_found_error(error=error)

@app.errorhandler(500)
def internal_error(error):
    return err.internal_error(error=error)

@app.errorhandler(405)
def method_not_allowed(error):
    return err.method_not_allowed(error=error)

@app.errorhandler(400)
def bad_request(error):
    return err.bad_request(error=error)

# Muat variabel lingkungan dari file .env
load_dotenv()

# Generate a secure random key
app.secret_key = os.getenv("SECRET_KEY")  # Menghasilkan kunci dengan panjang 16 byte

# Registrasi blueprint
app.register_blueprint(web_routes)
app.register_blueprint(api_routes)

if __name__ == '__main__':
    # Mendapatkan nilai dari variabel lingkungan
    app_name = os.getenv("APP_NAME")
    debug_mode = os.getenv("APP_DEBUG")
    host_ip = os.getenv("APP_HOST")
    app_port = os.getenv("APP_PORT")  # Menambah variabel untuk port

    # Menentukan host dan port berdasarkan mode (development/production)
    host = ''
    if debug_mode == 'development':
        host = str(host_ip)
        port = 5000 if app_port is None else int(app_port)
    else:
        host = str(host_ip)
        port = 80 if app_port is None else int(app_port)

    app.run(debug=True if debug_mode == 'development' else False, host=host, port=port)
