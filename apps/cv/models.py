from apps import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Cv(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Text, nullable=True)
    tanggal = db.Column(db.DateTime(timezone=True), default=func.now())