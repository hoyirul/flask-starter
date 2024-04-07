from flask import render_template

class WelcomeController:
    def index(self):
        return render_template('index.html')