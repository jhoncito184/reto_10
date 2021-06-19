from app import app
from flask import render_template
from app.menu.menuController import MenuController



@app.route('/menu')
def menu():
    return render_template('menu.html')
