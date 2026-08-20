from datetime import datetime
from extensions import db


class Merchant(db.Model):
    __tablename__ = "merchants"

    merchant_id = db.Column(db.Integer, primary_key=True)
    merchant_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), default="merchant", nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    stores = db.relationship(
        "Store",
        back_populates="merchant",
        cascade="all, delete-orphan"
    )

    admins = db.relationship(
        "StoreAdmin",
        back_populates="merchant",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Merchant {self.merchant_name}>"