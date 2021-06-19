from app import db
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.sql import func

class SalesModel(db.Model):
    __tablename__ = 'sales'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    total = db.Column(db.DECIMAL(10,2))
    fecha = db.Column(db.DateTime(timezone=True), server_default=func.now())
    
    #
    tax_id = db.Column(db.Integer, db.ForeignKey('tax.id'))
    salesType_id = db.Column(db.Integer, db.ForeignKey('salesType.id'))
    ##
    tax = db.relationship('TaxModel', uselist=False, back_populates='sales')
    salesType = db.relationship('SalesTypeModel', uselist=False, back_populates='sales') # [{}] -> {}

    def __repr__(self):
        return f'Sales: {self.id}'