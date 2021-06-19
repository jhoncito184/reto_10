from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SelectField, SubmitField
from wtforms.validators import DataRequired


class ProductsForm(FlaskForm):
    nombres = StringField('Titulo', validators=[DataRequired('Este campo es necesario')])
    descripcion = TextAreaField('Contenido', validators=[DataRequired('Este campo es necesario')])
    precio = StringField('Precio', validators=[DataRequired('Este campo es necesario')])
    category_id = SelectField('Categoria', coerce=int, 
                    validators=[DataRequired('Este campo es necesario')])
    submit = SubmitField('Enviar')
