from app import db
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.sql import func



class PublicationsModel(db.Model):
    __tablename__ = 'publications'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), index=True)
    content = db.Column(TEXT)
    image = db.Column(db.String(200))
    date_publish = db.Column(db.DateTime(timezone=True))
    status = db.Column(db.Integer, index=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now()) # SELECT NOW()
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    #
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    ##
    category = db.relationship('CategoriesModel', uselist=False, back_populates='publications') # [{}] -> {}
    user = db.relationship('UserModel', uselist=False, back_populates='publications') # [{}] -> {}

    def __repr__(self):
        return f'Publication: {self.title}'
