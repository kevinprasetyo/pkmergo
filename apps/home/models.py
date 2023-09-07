from apps import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=True)
    email = db.Column(db.Text, nullable=False)
    nama = db.Column(db.Text, nullable=True)
    pekerjaan = db.Column(db.Text, nullable=True)
