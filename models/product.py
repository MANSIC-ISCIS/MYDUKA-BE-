from datetime import datetime
from db import db #importing 'shared SQLAlchemy

class Supplier(db.Model):
    __tablename__ = 