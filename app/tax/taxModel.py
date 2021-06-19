from app import db


class TaxModel(db.Model):
    __tablename__ = 'tax'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    valor = db.Column(db.String(120), index=True)
    status = db.Column(db.Integer)

    def __repr__(self):
        return f'Tax: {self.valor}'
