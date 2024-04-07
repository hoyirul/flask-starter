
from flask import render_template, request, redirect, session, flash
import pandas as pd
import numpy as np
from app.models.user_model import UserModel

class UserController:
    def __init__(self):
        self.userModel = UserModel()
    
    def index(self):
        try:
            data = { 
                'title': 'UserController',
                'data': self.userModel.findAll(),
             }
            return render_template('pages/users/index.html', data=data)
        except Exception as e:
            return str(e)
    
    def create(self):
        try:
            return render_template('pages/users/create.html')
        except Exception as e:
            return str(e)
    
    def store(self):
        try:
            data = request.form.to_dict()
            self.userModel.create(data)
            return redirect('/users')
        except Exception as e:
            return str(e)
    
    def show(self, id):
        try:
            data = self.userModel.findById(id)
            return render_template('users/show.html', data=data)
        except Exception as e:
            return str(e)

    def edit(self, id):
        try:
            data = self.userModel.findById(id)
            return render_template('users/edit.html', data=data)
        except Exception as e:
            return str(e)

    def update(self, id):
        try:
            data = request.form.to_dict()
            self.userModel.update(id, data)
            return redirect('/users')
        except Exception as e:
            return str(e)
    
    def destroy(self, id):
        try:
            self.userModel.delete(id)
            return redirect('/users')
        except Exception as e:
            return str(e)
