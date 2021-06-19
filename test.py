from app import db
from app.user.userModel import UserModel

try:
    usuario = UserModel(username='admin', password='123456')
    usuario.hash_password()
    db.session.add(usuario)
    db.session.commit()
else:
    db.session.rollback()
