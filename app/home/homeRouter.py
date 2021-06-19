from app import app
from flask import render_template, send_from_directory
from flask_login import login_required
from app.menu.menuController import MenuController
from pathlib import Path


@app.route('/')
@login_required
def index():
    return render_template('views/home/index.html', title='Inicio')


@app.route('/uploads/<filename>')
def uploads(filename):
    root_dir = Path(__file__).parent.parent.parent
    upload_dir = root_dir / 'resources/uploads'
    return send_from_directory(upload_dir, filename)


@app.before_request
def before_request():
    controller = MenuController()
    controller.get_all()
