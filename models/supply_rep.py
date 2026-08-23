from datetime import datetime
from extensions import db

class SupplyRequest(db.Model):
    __tablename__ = 'supply_requests'

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.Text, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), nullable=False)
    store_name = db.Column(db.Text, nullable=True)
    store_id = db.Column(db.Integer, db.ForeignKey('store.store_id'), nullable=True)
    clerk_name = db.Column(db.Text, nullable=True)
    clerk_id = db.Column(db.Integer, db.ForeignKey('clerk.clerk_id'), nullable=True)
    quantity_requested = db.Column(db.Integer, nullable=False)
    reason = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(50), default='Pending')   
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
   