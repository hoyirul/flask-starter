from flask import Blueprint, request
from controllers.user_controller import UserController
from controllers.about_controller import AboutController

main = Blueprint('main', __name__)
userController = UserController()
aboutController = AboutController()

@main.route('/user/<int:user_id>')
def get_user(user_id):
    return userController.get_user(user_id)

@main.route('/user/<int:user_id>/update', methods=['POST'])
def update_user(user_id):
    # Ambil data yang diperlukan dari request dan panggil fungsi update pada user_controller
    pass

@main.route('/about/<int:id>')
def get_about(id):
    return aboutController.get_about(id)

@main.route('/store', methods=['POST'])
def store():
    return userController.store()
