from app import db
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.sql import func

class ProductsModel(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombres = db.Column(db.String(100), index=True)
    descripcion = db.Column(TEXT)
    precio = db.Column(db.String(100))
    status = db.Column(db.Integer, index=True)

    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now()) # SELECT NOW()
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    
    #
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    ##
    category = db.relationship('CategoriesModel', uselist=False, back_populates='products') # [{}] -> {}

    def __repr__(self):
        return f'Publication: {self.nombres}'