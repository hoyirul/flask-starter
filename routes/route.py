from flask import Blueprint, request, redirect, session
from controllers.welcome_controller import WelcomeController
from controllers.auth_controller import AuthController
from controllers.compressor_af_controller import CompressorAfController
from controllers.theme_anomaly_controller import ThemeAnomalyController
from middlewares.middleware import AuthMiddleware

main = Blueprint('main', __name__)
welcomeController = WelcomeController()
authController = AuthController()
compressorAfController = CompressorAfController()
themeAnomalyController = ThemeAnomalyController()
authMiddleware = AuthMiddleware()

@main.route('/', methods=['GET'])
@authMiddleware.authorized
def index():
    return welcomeController.index()

@main.route('/login', methods=['GET'])
@authMiddleware.unauthorized
def login():
    return authController.index()

@main.route('/auth/login', methods=['POST'])
def auth_login():
    return authController.auth_login()

@main.route('/auth/logout', methods=['GET'])
def auth_logout():
    return authController.auth_logout()

@main.route('/compressor-af/<int:id>', methods=['GET', 'POST'])
@authMiddleware.authorized
def compressor_af(id):
    return compressorAfController.index(id)

@main.route('/theme-anomalies', methods=['GET', 'POST'])
@authMiddleware.authorized
def theme_anomalies():
    return themeAnomalyController.index()
