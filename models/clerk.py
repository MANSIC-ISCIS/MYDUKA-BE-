# Clerk Model
# Imports
from extensions import db

# Create a new Clerk class
class Clerk(db.Model):
    __tablename__ = 'clerks'
    clerk_id = db.Column(db.Integer, primary_key=True)
    clerk_name = db.Column(db.String(100), nullable=False)
    admin_id = db.Column(db.String(50), nullable=False)
    store_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
