from app import db


class MenuModel(db.Model):
    __tablename__ = 'menu' # flask migrate
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    url = db.Column(db.String(50))
    icon = db.Column(db.String(60))
    status = db.Column(db.Integer)

    def __repr__(self):
        return f'Menu: {self.name}'
