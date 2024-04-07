from flask import Blueprint, request, redirect, session
from app.controllers.welcome_controller import WelcomeController
from app.controllers.user_controller import UserController
# from controllers.auth_controller import AuthController
# from middlewares.middleware import AuthMiddleware

web_routes = Blueprint('web_routes', __name__)
# welcomeController = WelcomeController()
# authController = AuthController()
# authMiddleware = AuthMiddleware()

@web_routes.route('/', methods=['GET'])
# @authMiddleware.authorized
def index():
    return WelcomeController().index()

# @web_routes.route('/login', methods=['GET'])
# # @authMiddleware.unauthorized
# def login():
#     return authController.index()

# @web_routes.route('/auth/login', methods=['POST'])
# def auth_login():
#     return authController.auth_login()

# @web_routes.route('/auth/logout', methods=['GET'])
# def auth_logout():
#     return authController.auth_logout()

@web_routes.route('/users', methods=['GET'])
def user():
    return UserController().index()

@web_routes.route('/users/create', methods=['GET'])
def user_create():
    return UserController().create()

@web_routes.route('/users/store', methods=['POST'])
def user_store():
    return UserController().store()

@web_routes.route('/users/<int:id>', methods=['GET'])
def user_show(id):
    return UserController().show(id)

@web_routes.route('/users/<int:id>/edit', methods=['GET'])
def user_edit(id):
    return UserController().edit(id)

@web_routes.route('/users/<int:id>', methods=['PUT'])
def user_update(id):
    return UserController().update(id)

@web_routes.route('/users/<int:id>/delete', methods=['DELETE'])
def user_delete(id):
    return UserController().destroy(id)
