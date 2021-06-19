from app import db
from sqlalchemy.sql import func

class SalesTypeModel(db.Model):
    __tablename__ = 'salesType'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), index=True)

    sales = db.relationship('SalesModel', back_populates='salesType')

    def __repr__(self):
        return f'salesType: {self.name}'
