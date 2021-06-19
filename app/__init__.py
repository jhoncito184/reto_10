from flask import Flask
from pathlib import Path
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


root_dir = Path(__file__).parent.parent
template_dir = root_dir / 'resources/templates'
static_dir = root_dir / 'resources/static'


app = Flask(__name__, template_folder=template_dir, \
                static_folder=static_dir, static_url_path='/static')
app.config.from_object(Config)

login = LoginManager(app)
login.login_view = 'login'
login.login_message = 'Debe iniciar sesión para acceder a la página'

db = SQLAlchemy(app)
''''
Migraciones
-----------
Cuando no tienes iniciada la migracion: flask db init (unica vez)
Cuando importamos un modelo (sea nuevo o reciente): flask db migrate -m "Comentario"
Para ejecutar la migracion: flask db upgrade
'''
migrate = Migrate(app, db)
