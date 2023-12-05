from flask import render_template

class AboutController:
    def get_about(self, id):
        print('Get User')
        return render_template('about.html')

    def update_user(self, id, data):
        print('Update User')
        pass
