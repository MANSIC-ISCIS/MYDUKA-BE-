from datetime import datetime
from extension import db

class SupplyRequest(db.Model):
    __tablename__ = 'supply_requests'

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.Text, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)
    store_name = db.Column(db.Text, nullable=True)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.store_id'), nullable=True)
    clerk_name = db.Column(db.Text, nullable=True)
    clerk_id = db.Column(db.Integer, db.ForeignKey('clerks.clerks_id'), nullable=True)
    quantity_requested = db.Column(db.Integer, nullable=False)
    reason = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(50), default='Pending')
  
