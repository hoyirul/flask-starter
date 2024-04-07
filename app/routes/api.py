from flask import Blueprint, request, redirect, session
from app.controllers.welcome_controller import WelcomeController
# from controllers.auth_controller import AuthController
# from middlewares.middleware import AuthMiddleware

api_routes = Blueprint('api_routes', __name__)
welcomeController = WelcomeController()
# authController = AuthController()
# authMiddleware = AuthMiddleware()

@api_routes.route('/', methods=['GET'])
# @authMiddleware.authorized
def index():
    return welcomeController.index()

# @api_routes.route('/login', methods=['GET'])
# # @authMiddleware.unauthorized
# def login():
#     return authController.index()

# @api_routes.route('/auth/login', methods=['POST'])
# def auth_login():
#     return authController.auth_login()

# @api_routes.route('/auth/logout', methods=['GET'])
# def auth_logout():
#     return authController.auth_logout()

