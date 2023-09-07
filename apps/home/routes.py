# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request, flash, redirect
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound
from apps.home.models import Profile, Hasil
from apps import db


@blueprint.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index')


@blueprint.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    try:
        if request.method == 'POST':
            username = request.form.get('username')
            email = request.form.get('email')
            nama = request.form.get('nama')
            pekerjaan = request.form.get('pekerjaan')

            profile = Profile(username=username, email=email,
                              nama=nama, pekerjaan=pekerjaan)
            db.session.add(profile)
            db.session.commit()
            flash("Berhasil tersimpan")
            return render_template('home/profile.html', segment='profile', profile=profile)
        else:
            profile = Profile.query.filter_by(
                email=current_user.email).order_by(Profile.id.desc()).first()
            return render_template('home/profile.html', segment='profile', profile=profile)
    except:
        return render_template('home/profile.html', segment='profile')


@blueprint.route('/gotrak/lihat', methods=['GET', 'POST'])
@login_required
def lihat():
    if request.method == 'POST':
        perusahaan = request.form.get('perusahaan')
        nama = request.form.get('nama')
        posisi = request.form.get('posisi')
        email = request.form.get('email')

        tugas1 = request.form.get('tugas1')
        tugas2 = request.form.get('tugas2')
        tugas3 = request.form.get('tugas3')

        waktu1 = request.form.get('waktu1')
        waktu2 = request.form.get('waktu2')
        waktu3 = request.form.get('waktu3')

        tgn1 = request.form.get('tgn')
        tgn2 = request.form.get('tgn2')

        if tgn2 == None and tgn1 == None:
            tgn = None
        elif tgn2 == None:
            tgn = tgn1
        elif tgn1 == None:
            tgn = tgn2
        else:
            tgn = f"{tgn1} dan {tgn2}"

        lama = request.form.get('lama')
        mental = request.form.get('mental')
        fisik = request.form.get('fisik')
        sakit = request.form.get('sakit')

        pilih1 = request.form.get('pilih1')
        pilih2 = request.form.get('pilih2')
        pilih3 = request.form.get('pilih3')
        pilih4 = request.form.get('pilih4')
        pilih5 = request.form.get('pilih5')
        pilih6 = request.form.get('pilih6')
        pilih7 = request.form.get('pilih7')
        pilih8 = request.form.get('pilih8')
        pilih9 = request.form.get('pilih9')
        pilih10 = request.form.get('pilih10')
        pilih11 = request.form.get('pilih11')
        pilih12 = request.form.get('pilih12')

        list = [pilih1, pilih2, pilih3, pilih4, pilih5, pilih6,
                pilih7, pilih8, pilih9, pilih10, pilih11, pilih12]
        ada = []
        for i in list:
            if i != None:
                ada.append(i)

        bagian = ', '.join([str(x) for x in ada])

        seringleher = request.form.get('seringleher')
        leher = request.form.get('leher')
        seringbahu = request.form.get('seringbahu')
        bahu = request.form.get('bahu')
        seringpa = request.form.get('seringpa')
        pa = request.form.get('pa')
        bagiansiku = request.form.get('bagiansiku')
        seringsiku = request.form.get('seringsiku')
        siku = request.form.get('siku')
        seringpb = request.form.get('seringpb')
        pb = request.form.get('pb')
        bagianlengan = request.form.get('bagianlengan')
        seringlengan = request.form.get('seringlengan')
        lengan = request.form.get('lengan')
        bagiantanggan = request.form.get('bagiantanggan')
        seringtangan = request.form.get('seringtangan')
        tangan = request.form.get('tangan')
        bagianpinggul = request.form.get('bagianpinggul')
        seringpinggul = request.form.get('seringpinggul')
        pinggul = request.form.get('pinggul')
        bagianpaha = request.form.get('bagianpaha')
        seringpaha = request.form.get('seringpaha')
        paha = request.form.get('paha')
        bagianlutut = request.form.get('bagianlutut')
        seringlutut = request.form.get('seringlutut')
        lutut = request.form.get('lutut')
        bagianbetis = request.form.get('bagianbetis')
        seringbetis = request.form.get('seringbetis')
        betis = request.form.get('betis')
        bagiankaki = request.form.get('bagiankaki')
        seringkaki = request.form.get('seringkaki')
        kaki = request.form.get('kaki')

        if seringleher == "tidak pernah" and leher == "tidak ada masalah":
            SKORLEHER = 1
        elif seringleher == "tidak pernah" and leher == "tidak nyaman":
            SKORLEHER = 2
        elif seringleher == "tidak pernah" and leher == "sakit":
            SKORLEHER = 3
        elif seringleher == "tidak pernah" and leher == "sakit parah":
            SKORLEHER = 4
        if seringleher == "terkadang" and leher == "tidak ada masalah":
            SKORLEHER = 2
        elif seringleher == "terkadang" and leher == "tidak nyaman":
            SKORLEHER = 4
        elif seringleher == "terkadang" and leher == "sakit":
            SKORLEHER = 6
        elif seringleher == "terkadang" and leher == "sakit parah":
            SKORLEHER = 8
        if seringleher == "sering" and leher == "tidak ada masalah":
            SKORLEHER = 3
        elif seringleher == "sering" and leher == "tidak nyaman":
            SKORLEHER = 6
        elif seringleher == "sering" and leher == "sakit":
            SKORLEHER = 9
        elif seringleher == "sering" and leher == "sakit parah":
            SKORLEHER = 12
        if seringleher == "selalu" and leher == "tidak ada masalah":
            SKORLEHER = 4
        elif seringleher == "selalu" and leher == "tidak nyaman":
            SKORLEHER = 8
        elif seringleher == "selalu" and leher == "sakit":
            SKORLEHER = 12
        elif seringleher == "selalu" and leher == "sakit parah":
            SKORLEHER = 16
        elif seringleher == "sering":
            SKORLEHER = 99
        else:
            SKORLEHER = 0

        gotrak = Hasil(perusahaan=perusahaan, nama=nama, posisi=posisi, email=email, tugas1=tugas1, tugas2=tugas2, tugas3=tugas3,
                       waktu1=waktu1, waktu2=waktu2, waktu3=waktu3, tgn=tgn, lama=lama, mental=mental, fisik=fisik, sakit=sakit, bagian=bagian, seringleher=seringleher, leher=leher, skorleher=SKORLEHER)
        db.session.add(gotrak)
        db.session.commit()
        flash("Berhasil tersimpan")
        return render_template('home/lihat.html', segment='lihat', gotrak=gotrak)
    elif "lihat" in request.args:
        id = request.args.get('lihat')
        gotrak = Hasil.query.filter_by(id=id).one()
        return render_template('home/lihat.html', segment='lihat', gotrak=gotrak)
    else:
        return render_template('home/gotrak.html', segment='gotrak')


@blueprint.route('/hasil/', methods=['GET', 'POST'])
@login_required
def hasil():
    if "hapus" in request.args:
        id = request.args.get('hapus')
        hasil = Hasil.query.filter_by(id=id).one()
        email = hasil.email
        db.session.delete(hasil)
        db.session.commit()
        flash("Berhasil dihapus")
        return redirect(f'/hasil/{email}')
    gotrak = Hasil.query.all()
    return render_template('home/hasil.html', segment='hasil', gotrak=gotrak)


@blueprint.route('/hasil/<email>', methods=['GET', 'POST'])
@login_required
def hasildari(email):
    gotrak = Hasil.query.filter_by(email=email).all()
    return render_template('home/hasil.html', segment='hasil', gotrak=gotrak)


@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
