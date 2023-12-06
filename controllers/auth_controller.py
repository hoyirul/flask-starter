from flask import render_template, request, redirect, session, flash
import requests
from utils.handler_api import endpoint_login

class AuthController:
    def index(self):
        return render_template('auth/auth.html')

    def auth_login(self):
        nik = request.form['nik']
        password = request.form['password']

        payload = {'nik': nik, 'password': password}
        headers = {'Content-Type': 'application/json'}
        
        response = requests.post(endpoint_login, json=payload, headers=headers)
        
        if response.status_code == 200:
            session['nik'] = nik
            session['token'] = response.json().get('token')  # Menggunakan get untuk menghindari KeyError
            session['logged_in'] = True
            return redirect('/')  # Redirect setelah login berhasil
        else:
            flash(response.json().get('message'), 'danger')
            return redirect('/login')
    
    def auth_logout(self):
        session.clear()
        return redirect('/login')
