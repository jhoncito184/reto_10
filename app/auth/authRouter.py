from app import app
from flask import render_template, redirect, url_for
from app.auth.authController import AuthController
from flask_login import login_required, logout_user



@app.route('/login', methods=['GET', 'POST'])
def login():
    controller = AuthController()
    return controller.auth_login()


@app.route('/register', methods=['GET', 'POST'])
def register():
    controller = AuthController()
    return controller.auth_register()


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
