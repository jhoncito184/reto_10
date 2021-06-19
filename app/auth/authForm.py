from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired('Este campo es requerido')])
    password = PasswordField('Contraseña', validators=[DataRequired('Este campo es requerido')])
    submit = SubmitField('Ingresar')


class RegisterForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired('Este campo es requerido')])
    password = PasswordField('Contraseña', validators=[
                            DataRequired('Este campo es requerido'),
                            EqualTo('password_confirm', message='Las contraseñas no son iguales')
                        ])
    password_confirm = PasswordField('Confirmar Contraseña', 
                            validators=[DataRequired('Este campo es requerido')])
    submit = SubmitField('Registrar')
