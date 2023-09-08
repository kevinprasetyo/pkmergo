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
    skorleher = db.Column(db.Text, nullable=True)
    nilaileher = db.Column(db.Text, nullable=True)
    skorbahu = db.Column(db.Text, nullable=True)
    nilaibahu = db.Column(db.Text, nullable=True)
    skorpa = db.Column(db.Text, nullable=True)
    nilaipa = db.Column(db.Text, nullable=True)
    skorsiku = db.Column(db.Text, nullable=True)
    nilaisiku = db.Column(db.Text, nullable=True)
    skorpb = db.Column(db.Text, nullable=True)
    nilaipb = db.Column(db.Text, nullable=True)
    skorlengan = db.Column(db.Text, nullable=True)
    nilailengan = db.Column(db.Text, nullable=True)
    skortangan = db.Column(db.Text, nullable=True)
    nilaitangan = db.Column(db.Text, nullable=True)
    skorpinggul = db.Column(db.Text, nullable=True)
    nilaipinggul = db.Column(db.Text, nullable=True)
    skorpaha = db.Column(db.Text, nullable=True)
    nilaipaha = db.Column(db.Text, nullable=True)
    skorlutut = db.Column(db.Text, nullable=True)
    nilailutut = db.Column(db.Text, nullable=True)
    skorbetis = db.Column(db.Text, nullable=True)
    nilaibetis = db.Column(db.Text, nullable=True)
    skorkaki = db.Column(db.Text, nullable=True)
    nilaikaki = db.Column(db.Text, nullable=True)


class Janji(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.Text, nullable=True)
    email = db.Column(db.Text, nullable=False)
    hp = db.Column(db.Text, nullable=True)
    tgl = db.Column(db.Text, nullable=True)
