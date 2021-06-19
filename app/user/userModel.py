from app import db, login
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.sql import func



class UserModel(UserMixin, db.Model): # user_models
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(150))
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now()) # SELECT NOW()
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    #
    rol = db.relationship('RolesModel', uselist=False, back_populates='users')
    ##
    publications = db.relationship('PublicationsModel', back_populates='user')

    def __repr__(self):
        return f'User: {self.username}'

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


# Obtiene los datos del usuario cuando se conecte
@login.user_loader
def load_user(user_id):
    return UserModel.query.get(int(user_id))
