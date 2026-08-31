from extensions import db


class StoreAdmin(db.Model):
    __tablename__ = "store_admin"

    admin_id = db.Column(
        db.Integer,
        primary_key=True
    )

    admin_name = db.Column(
        db.String(100),
        nullable=False
    )

    merchant_id = db.Column(
        db.Integer,
        db.ForeignKey("merchants.merchant_id"),
        nullable=False
    )

    store_id = db.Column(
        db.Integer,
        db.ForeignKey("store.store_id"),
        nullable=False
    )

    is_active = db.Column(
        db.Boolean,
        default=True,
        nullable=False
    )

    def __repr__(self):
        return f"<StoreAdmin {self.admin_name}>"