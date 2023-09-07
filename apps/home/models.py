from apps import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=True)
    email = db.Column(db.Text, nullable=False)
    nama = db.Column(db.Text, nullable=True)
    pekerjaan = db.Column(db.Text, nullable=True)


class Hasil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    perusahaan = db.Column(db.Text, nullable=True)
    tanggal = db.Column(db.DateTime(timezone=True), default=func.now())
    nama = db.Column(db.Text, nullable=True)
    posisi = db.Column(db.Text, nullable=True)
    email = db.Column(db.Text, nullable=True)
    tugas1 = db.Column(db.Text, nullable=True)
    tugas2 = db.Column(db.Text, nullable=True)
    tugas3 = db.Column(db.Text, nullable=True)
    waktu1 = db.Column(db.Integer, nullable=True)
    waktu2 = db.Column(db.Integer, nullable=True)
    waktu3 = db.Column(db.Integer, nullable=True)
    tgn = db.Column(db.Text, nullable=True)
    lama = db.Column(db.Text, nullable=True)
    mental = db.Column(db.Text, nullable=True)
    fisik = db.Column(db.Text, nullable=True)
    sakit = db.Column(db.Text, nullable=True)
    bagian = db.Column(db.Text, nullable=True)
