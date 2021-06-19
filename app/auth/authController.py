from app import db
from flask import render_template, redirect, url_for, flash
from app.auth.authForm import LoginForm, RegisterForm
from app.user.userModel import UserModel
from flask_login import login_user, current_user


class AuthController:
    def __init__(self):
        self.current_user = current_user

    def auth_login(self):
        if self.current_user.is_authenticated:
            return redirect(url_for('index'))

        form_login = LoginForm()
        # POST
        if form_login.validate_on_submit():
            username = form_login.username.data
            password = form_login.password.data
            # Buscando Usuario (Exista)
            user = UserModel.query.filter_by(username=username).first() # None
            # SQL -> SELECT * FROM users WHERE username = 'username'
            # Si el usuario no existe o contraseña erronea
            if user is None or not user.check_password(password):
                flash('Usuario y/o contraseña son incorrectos', 'danger')
                return redirect(url_for('login'))
            # Autenticacion correcta
            login_user(user)
            return redirect(url_for('index'))
        return render_template('views/auth/login.html', title='Login', form=form_login)

    def auth_register(self):
        form_register = RegisterForm()
        if form_register.validate_on_submit():
            username = form_register.username.data
            password = form_register.password.data

            # Validamos que el usuario no exista
            user = UserModel.query.filter_by(username=username).first()
            if user:
                flash(f'El usuario {username} ya existe, pruebe con otro !', 'danger')
                return redirect(url_for('register'))
            
            # Creación de un usuario
            user_add = UserModel(username=username, password=password, rol_id=2)
            user_add.hash_password()
            db.session.add(user_add)
            db.session.commit()

            flash(f'El usuario {username} se creo con exito !', 'success')
            return redirect(url_for('login'))
        return render_template('views/auth/register.html', title='Register', form=form_register)
