from datetime import datetime
from db import db #importing 'shared SQLAlchemy

class Supplier(db.Model):
    __tablename__ = 'suppliers'

    supplier_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)
    email = db.Column(db.string(120), nullable=True)
    address = db.Column(db.String(255), nullable=True)

    #   Relationship to products supplied 
    products = db.relationship('Product', backref='supplier', lazy=True)
    