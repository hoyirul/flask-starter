from flask import Blueprint, request, redirect, session
from controllers.user_controller import UserController
from controllers.about_controller import AboutController
from controllers.welcome_controller import WelcomeController
from controllers.auth_controller import AuthController
from controllers.compressor_af_controller import CompressorAfController
from middlewares.middleware import AuthMiddleware

main = Blueprint('main', __name__)
userController = UserController()
aboutController = AboutController()
welcomeController = WelcomeController()
authController = AuthController()
compressorAfController = CompressorAfController()
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

@main.route('/compressors', methods=['GET'])
def compressors():
    return compressorAfController.index()

@main.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return userController.get_user(user_id)

@main.route('/user/<int:user_id>/update', methods=['POST'])
def update_user(user_id):
    # Ambil data yang diperlukan dari request dan panggil fungsi update pada user_controller
    pass

@main.route('/about/<int:id>', methods=['GET'])
def get_about(id):
    return aboutController.get_about(id)

@main.route('/store', methods=['POST'])
def store():
    return userController.store()
