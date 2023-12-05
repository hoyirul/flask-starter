from flask import render_template, request, redirect, session
import requests

class AuthController:
    def index(self):
        return render_template('auth/auth.html')

    def auth_login(self):
        nik = request.form['nik']
        password = request.form['password']

        api_url = 'http://192.168.9.47:3270/users/login'
        payload = {'nik': nik, 'password': password}
        headers = {'Content-Type': 'application/json'}
        
        response = requests.post(api_url, json=payload, headers=headers)
        
        if response.status_code == 200:
            session['nik'] = nik
            session['token'] = response.json().get('token')  # Menggunakan get untuk menghindari KeyError
            session['logged_in'] = True
            return redirect('/dashboard')  # Redirect setelah login berhasil
        else:
            session['errors'] = 'Login gagal, cek username dan password!'
            return redirect('/')
    
    def auth_logout(self):
        pass
