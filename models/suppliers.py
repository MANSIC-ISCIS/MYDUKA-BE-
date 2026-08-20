from datetime import datetime
from db import db  # Importing shared SQLAlchemy instance

class Supplier(db.Model):
    __tablename__ = 'suppliers'

    supplier_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    address = db.Column(db.String(255), nullable=True)

    # Relationship to products supplied
    products = db.relationship('Product', backref='supplier', lazy=True)