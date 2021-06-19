from app import db


class SalesTypeModel(db.Model):
    __tablename__ = 'salesType'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), index=True)

    def __repr__(self):
        return f'salesType: {self.name}'
