from app import db


class ProductModel(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), index=True)
    status = db.Column(db.Integer)

    def __repr__(self):
        return f'Tax: {self.name}'
