from app import db
from sqlalchemy.sql import func



class CategoriesModel(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), index=True)
    status = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now()) # SELECT NOW()
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    #
    publications = db.relationship('PublicationsModel', back_populates='category')

    def __repr__(self):
        return f'Category: {self.name}'
