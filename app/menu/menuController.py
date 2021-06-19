from app.menu.menuModel import MenuModel
from flask import g


class MenuController:
    def get_all(self):
        # fetch_all
        # fetch_one
        records = MenuModel.query.filter_by(status=1).all() # first()
        g.menu = records
