from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SelectField, SubmitField
from wtforms.validators import DataRequired


class PublicationsForm(FlaskForm):
    title = StringField('Titulo', validators=[DataRequired('Este campo es necesario')])
    content = TextAreaField('Contenido', validators=[DataRequired('Este campo es necesario')])
    image = FileField('Imagen')
    category_id = SelectField('Categoria', coerce=int, 
                    validators=[DataRequired('Este campo es necesario')])
    submit = SubmitField('Enviar')
