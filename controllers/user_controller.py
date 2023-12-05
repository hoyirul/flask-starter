from flask import render_template, jsonify, request

class UserController:
    def get_user(self, user_id):
        print('Get User')
        return render_template('index.html')

    def store(self):
        name = request.form['name']
        return render_template('index.html', data=name)
        
