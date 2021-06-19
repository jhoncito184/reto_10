from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class TaxForm(FlaskForm):
    valor = StringField('Valor', validators=[DataRequired('Este campo es requerido')])
    submit = SubmitField('Enviar')
