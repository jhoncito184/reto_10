from app import db


class RolesModel(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), index=True)
    ##
    users = db.relationship('UserModel', back_populates='rol')

    def __repr__(self):
        return f'Rol: {self.name}'
