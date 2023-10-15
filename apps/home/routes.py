from apps.home import blueprint
from flask import render_template, request, flash, redirect
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound
from apps.home.models import Profile, Hasil
from apps.authentication.models import Users
from apps import db


@blueprint.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index')


@blueprint.route('/profile', methods=['GET', 'POST'])
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


@blueprint.route('/profile/<username>', methods=['GET', 'POST'])
@login_required
def hapusakun(username):
    try:
        if request.method == 'POST':
            konfirmasi = request.form.get('konfirmasi')
            konfirmasi = konfirmasi.lower()
            if konfirmasi == "hapus akun":
                hapus = Users.query.filter_by(username=username).one()
                db.session.delete(hapus)
                db.session.commit()
                flash("Akun berhasil dihapus!")
                return redirect('/logout')
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

        # Leher
        if seringleher == "tidak pernah" and leher == "tidak ada masalah":
            skorleher = 1
        elif seringleher == "tidak pernah" and leher == "tidak nyaman":
            skorleher = 2
        elif seringleher == "tidak pernah" and leher == "sakit":
            skorleher = 3
        elif seringleher == "tidak pernah" and leher == "sakit parah":
            skorleher = 4
        elif seringleher == "terkadang" and leher == "tidak ada masalah":
            skorleher = 2
        elif seringleher == "terkadang" and leher == "tidak nyaman":
            skorleher = 4
        elif seringleher == "terkadang" and leher == "sakit":
            skorleher = 6
        elif seringleher == "terkadang" and leher == "sakit parah":
            skorleher = 8
        elif seringleher == "sering" and leher == "tidak ada masalah":
            skorleher = 3
        elif seringleher == "sering" and leher == "tidak nyaman":
            skorleher = 6
        elif seringleher == "sering" and leher == "sakit":
            skorleher = 9
        elif seringleher == "sering" and leher == "sakit parah":
            skorleher = 12
        elif seringleher == "selalu" and leher == "tidak ada masalah":
            skorleher = 4
        elif seringleher == "selalu" and leher == "tidak nyaman":
            skorleher = 8
        elif seringleher == "selalu" and leher == "sakit":
            skorleher = 12
        elif seringleher == "selalu" and leher == "sakit parah":
            skorleher = 16
        else:
            skorleher = 0

        if skorleher < 2:
            nilaileher = "aman"
        elif skorleher < 7:
            nilaileher = "perlu pengamatan lebih lanjut"
        else:
            nilaileher = "bahaya"

        # Siku
        if seringbahu == "tidak pernah" and bahu == "tidak ada masalah":
            skorbahu = 1
        elif seringbahu == "tidak pernah" and bahu == "tidak nyaman":
            skorbahu = 2
        elif seringbahu == "tidak pernah" and bahu == "sakit":
            skorbahu = 3
        elif seringbahu == "tidak pernah" and bahu == "sakit parah":
            skorbahu = 4
        elif seringbahu == "terkadang" and bahu == "tidak ada masalah":
            skorbahu = 2
        elif seringbahu == "terkadang" and bahu == "tidak nyaman":
            skorbahu = 4
        elif seringbahu == "terkadang" and bahu == "sakit":
            skorbahu = 6
        elif seringbahu == "terkadang" and bahu == "sakit parah":
            skorbahu = 8
        elif seringbahu == "sering" and bahu == "tidak ada masalah":
            skorbahu = 3
        elif seringbahu == "sering" and bahu == "tidak nyaman":
            skorbahu = 6
        elif seringbahu == "sering" and bahu == "sakit":
            skorbahu = 9
        elif seringbahu == "sering" and bahu == "sakit parah":
            skorbahu = 12
        elif seringbahu == "selalu" and bahu == "tidak ada masalah":
            skorbahu = 4
        elif seringbahu == "selalu" and bahu == "tidak nyaman":
            skorbahu = 8
        elif seringbahu == "selalu" and bahu == "sakit":
            skorbahu = 12
        elif seringbahu == "selalu" and bahu == "sakit parah":
            skorbahu = 16
        else:
            skorbahu = 0

        if skorbahu < 2:
            nilaibahu = "aman"
        elif skorbahu < 7:
            nilaibahu = "perlu pengamatan lebih lanjut"
        else:
            nilaibahu = "bahaya"

        # PA
        if seringpa == "tidak pernah" and pa == "tidak ada masalah":
            skorpa = 1
        elif seringpa == "tidak pernah" and pa == "tidak nyaman":
            skorpa = 2
        elif seringpa == "tidak pernah" and pa == "sakit":
            skorpa = 3
        elif seringpa == "tidak pernah" and pa == "sakit parah":
            skorpa = 4
        elif seringpa == "terkadang" and pa == "tidak ada masalah":
            skorpa = 2
        elif seringpa == "terkadang" and pa == "tidak nyaman":
            skorpa = 4
        elif seringpa == "terkadang" and pa == "sakit":
            skorpa = 6
        elif seringpa == "terkadang" and pa == "sakit parah":
            skorpa = 8
        elif seringpa == "sering" and pa == "tidak ada masalah":
            skorpa = 3
        elif seringpa == "sering" and pa == "tidak nyaman":
            skorpa = 6
        elif seringpa == "sering" and pa == "sakit":
            skorpa = 9
        elif seringpa == "sering" and pa == "sakit parah":
            skorpa = 12
        elif seringpa == "selalu" and pa == "tidak ada masalah":
            skorpa = 4
        elif seringpa == "selalu" and pa == "tidak nyaman":
            skorpa = 8
        elif seringpa == "selalu" and pa == "sakit":
            skorpa = 12
        elif seringpa == "selalu" and pa == "sakit parah":
            skorpa = 16
        else:
            skorpa = 0

        if skorpa < 2:
            nilaipa = "aman"
        elif skorpa < 7:
            nilaipa = "perlu pengamatan lebih lanjut"
        else:
            nilaipa = "bahaya"

        # Siku
        if seringsiku == "tidak pernah" and siku == "tidak ada masalah":
            skorsiku = 1
        elif seringsiku == "tidak pernah" and siku == "tidak nyaman":
            skorsiku = 2
        elif seringsiku == "tidak pernah" and siku == "sakit":
            skorsiku = 3
        elif seringsiku == "tidak pernah" and siku == "sakit parah":
            skorsiku = 4
        elif seringsiku == "terkadang" and siku == "tidak ada masalah":
            skorsiku = 2
        elif seringsiku == "terkadang" and siku == "tidak nyaman":
            skorsiku = 4
        elif seringsiku == "terkadang" and siku == "sakit":
            skorsiku = 6
        elif seringsiku == "terkadang" and siku == "sakit parah":
            skorsiku = 8
        elif seringsiku == "sering" and siku == "tidak ada masalah":
            skorsiku = 3
        elif seringsiku == "sering" and siku == "tidak nyaman":
            skorsiku = 6
        elif seringsiku == "sering" and siku == "sakit":
            skorsiku = 9
        elif seringsiku == "sering" and siku == "sakit parah":
            skorsiku = 12
        elif seringsiku == "selalu" and siku == "tidak ada masalah":
            skorsiku = 4
        elif seringsiku == "selalu" and siku == "tidak nyaman":
            skorsiku = 8
        elif seringsiku == "selalu" and siku == "sakit":
            skorsiku = 12
        elif seringsiku == "selalu" and siku == "sakit parah":
            skorsiku = 16
        else:
            skorsiku = 0

        if skorsiku < 2:
            nilaisiku = "aman"
        elif skorsiku < 7:
            nilaisiku = "perlu pengamatan lebih lanjut"
        else:
            nilaisiku = "bahaya"

        # PB
        if seringpb == "tidak pernah" and pb == "tidak ada masalah":
            skorpb = 1
        elif seringpb == "tidak pernah" and pb == "tidak nyaman":
            skorpb = 2
        elif seringpb == "tidak pernah" and pb == "sakit":
            skorpb = 3
        elif seringpb == "tidak pernah" and pb == "sakit parah":
            skorpb = 4
        elif seringpb == "terkadang" and pb == "tidak ada masalah":
            skorpb = 2
        elif seringpb == "terkadang" and pb == "tidak nyaman":
            skorpb = 4
        elif seringpb == "terkadang" and pb == "sakit":
            skorpb = 6
        elif seringpb == "terkadang" and pb == "sakit parah":
            skorpb = 8
        elif seringpb == "sering" and pb == "tidak ada masalah":
            skorpb = 3
        elif seringpb == "sering" and pb == "tidak nyaman":
            skorpb = 6
        elif seringpb == "sering" and pb == "sakit":
            skorpb = 9
        elif seringpb == "sering" and pb == "sakit parah":
            skorpb = 12
        elif seringpb == "selalu" and pb == "tidak ada masalah":
            skorpb = 4
        elif seringpb == "selalu" and pb == "tidak nyaman":
            skorpb = 8
        elif seringpb == "selalu" and pb == "sakit":
            skorpb = 12
        elif seringpb == "selalu" and pb == "sakit parah":
            skorpb = 16
        else:
            skorpb = 0

        if skorpb < 2:
            nilaipb = "aman"
        elif skorpb < 7:
            nilaipb = "perlu pengamatan lebih lanjut"
        else:
            nilaipb = "bahaya"

        # lengan
        if seringlengan == "tidak pernah" and lengan == "tidak ada masalah":
            skorlengan = 1
        elif seringlengan == "tidak pernah" and lengan == "tidak nyaman":
            skorlengan = 2
        elif seringlengan == "tidak pernah" and lengan == "sakit":
            skorlengan = 3
        elif seringlengan == "tidak pernah" and lengan == "sakit parah":
            skorlengan = 4
        elif seringlengan == "terkadang" and lengan == "tidak ada masalah":
            skorlengan = 2
        elif seringlengan == "terkadang" and lengan == "tidak nyaman":
            skorlengan = 4
        elif seringlengan == "terkadang" and lengan == "sakit":
            skorlengan = 6
        elif seringlengan == "terkadang" and lengan == "sakit parah":
            skorlengan = 8
        elif seringlengan == "sering" and lengan == "tidak ada masalah":
            skorlengan = 3
        elif seringlengan == "sering" and lengan == "tidak nyaman":
            skorlengan = 6
        elif seringlengan == "sering" and lengan == "sakit":
            skorlengan = 9
        elif seringlengan == "sering" and lengan == "sakit parah":
            skorlengan = 12
        elif seringlengan == "selalu" and lengan == "tidak ada masalah":
            skorlengan = 4
        elif seringlengan == "selalu" and lengan == "tidak nyaman":
            skorlengan = 8
        elif seringlengan == "selalu" and lengan == "sakit":
            skorlengan = 12
        elif seringlengan == "selalu" and lengan == "sakit parah":
            skorlengan = 16
        else:
            skorlengan = 0

        if skorlengan < 2:
            nilailengan = "aman"
        elif skorlengan < 7:
            nilailengan = "perlu pengamatan lebih lanjut"
        else:
            nilailengan = "bahaya"

        # Tangan
        if seringtangan == "tidak pernah" and tangan == "tidak ada masalah":
            skortangan = 1
        elif seringtangan == "tidak pernah" and tangan == "tidak nyaman":
            skortangan = 2
        elif seringtangan == "tidak pernah" and tangan == "sakit":
            skortangan = 3
        elif seringtangan == "tidak pernah" and tangan == "sakit parah":
            skortangan = 4
        elif seringtangan == "terkadang" and tangan == "tidak ada masalah":
            skortangan = 2
        elif seringtangan == "terkadang" and tangan == "tidak nyaman":
            skortangan = 4
        elif seringtangan == "terkadang" and tangan == "sakit":
            skortangan = 6
        elif seringtangan == "terkadang" and tangan == "sakit parah":
            skortangan = 8
        elif seringtangan == "sering" and tangan == "tidak ada masalah":
            skortangan = 3
        elif seringtangan == "sering" and tangan == "tidak nyaman":
            skortangan = 6
        elif seringtangan == "sering" and tangan == "sakit":
            skortangan = 9
        elif seringtangan == "sering" and tangan == "sakit parah":
            skortangan = 12
        elif seringtangan == "selalu" and tangan == "tidak ada masalah":
            skortangan = 4
        elif seringtangan == "selalu" and tangan == "tidak nyaman":
            skortangan = 8
        elif seringtangan == "selalu" and tangan == "sakit":
            skortangan = 12
        elif seringtangan == "selalu" and tangan == "sakit parah":
            skortangan = 16
        else:
            skortangan = 0

        if skortangan < 2:
            nilaitangan = "aman"
        elif skortangan < 7:
            nilaitangan = "perlu pengamatan lebih lanjut"
        else:
            nilaitangan = "bahaya"

        # pinggul
        if seringpinggul == "tidak pernah" and pinggul == "tidak ada masalah":
            skorpinggul = 1
        elif seringpinggul == "tidak pernah" and pinggul == "tidak nyaman":
            skorpinggul = 2
        elif seringpinggul == "tidak pernah" and pinggul == "sakit":
            skorpinggul = 3
        elif seringpinggul == "tidak pernah" and pinggul == "sakit parah":
            skorpinggul = 4
        elif seringpinggul == "terkadang" and pinggul == "tidak ada masalah":
            skorpinggul = 2
        elif seringpinggul == "terkadang" and pinggul == "tidak nyaman":
            skorpinggul = 4
        elif seringpinggul == "terkadang" and pinggul == "sakit":
            skorpinggul = 6
        elif seringpinggul == "terkadang" and pinggul == "sakit parah":
            skorpinggul = 8
        elif seringpinggul == "sering" and pinggul == "tidak ada masalah":
            skorpinggul = 3
        elif seringpinggul == "sering" and pinggul == "tidak nyaman":
            skorpinggul = 6
        elif seringpinggul == "sering" and pinggul == "sakit":
            skorpinggul = 9
        elif seringpinggul == "sering" and pinggul == "sakit parah":
            skorpinggul = 12
        elif seringpinggul == "selalu" and pinggul == "tidak ada masalah":
            skorpinggul = 4
        elif seringpinggul == "selalu" and pinggul == "tidak nyaman":
            skorpinggul = 8
        elif seringpinggul == "selalu" and pinggul == "sakit":
            skorpinggul = 12
        elif seringpinggul == "selalu" and pinggul == "sakit parah":
            skorpinggul = 16
        else:
            skorpinggul = 0

        if skorpinggul < 2:
            nilaipinggul = "aman"
        elif skorpinggul < 7:
            nilaipinggul = "perlu pengamatan lebih lanjut"
        else:
            nilaipinggul = "bahaya"

        # paha
        if seringpaha == "tidak pernah" and paha == "tidak ada masalah":
            skorpaha = 1
        elif seringpaha == "tidak pernah" and paha == "tidak nyaman":
            skorpaha = 2
        elif seringpaha == "tidak pernah" and paha == "sakit":
            skorpaha = 3
        elif seringpaha == "tidak pernah" and paha == "sakit parah":
            skorpaha = 4
        elif seringpaha == "terkadang" and paha == "tidak ada masalah":
            skorpaha = 2
        elif seringpaha == "terkadang" and paha == "tidak nyaman":
            skorpaha = 4
        elif seringpaha == "terkadang" and paha == "sakit":
            skorpaha = 6
        elif seringpaha == "terkadang" and paha == "sakit parah":
            skorpaha = 8
        elif seringpaha == "sering" and paha == "tidak ada masalah":
            skorpaha = 3
        elif seringpaha == "sering" and paha == "tidak nyaman":
            skorpaha = 6
        elif seringpaha == "sering" and paha == "sakit":
            skorpaha = 9
        elif seringpaha == "sering" and paha == "sakit parah":
            skorpaha = 12
        elif seringpaha == "selalu" and paha == "tidak ada masalah":
            skorpaha = 4
        elif seringpaha == "selalu" and paha == "tidak nyaman":
            skorpaha = 8
        elif seringpaha == "selalu" and paha == "sakit":
            skorpaha = 12
        elif seringpaha == "selalu" and paha == "sakit parah":
            skorpaha = 16
        else:
            skorpaha = 0

        if skorpaha < 2:
            nilaipaha = "aman"
        elif skorpaha < 7:
            nilaipaha = "perlu pengamatan lebih lanjut"
        else:
            nilaipaha = "bahaya"

        # lutut
        if seringlutut == "tidak pernah" and lutut == "tidak ada masalah":
            skorlutut = 1
        elif seringlutut == "tidak pernah" and lutut == "tidak nyaman":
            skorlutut = 2
        elif seringlutut == "tidak pernah" and lutut == "sakit":
            skorlutut = 3
        elif seringlutut == "tidak pernah" and lutut == "sakit parah":
            skorlutut = 4
        elif seringlutut == "terkadang" and lutut == "tidak ada masalah":
            skorlutut = 2
        elif seringlutut == "terkadang" and lutut == "tidak nyaman":
            skorlutut = 4
        elif seringlutut == "terkadang" and lutut == "sakit":
            skorlutut = 6
        elif seringlutut == "terkadang" and lutut == "sakit parah":
            skorlutut = 8
        elif seringlutut == "sering" and lutut == "tidak ada masalah":
            skorlutut = 3
        elif seringlutut == "sering" and lutut == "tidak nyaman":
            skorlutut = 6
        elif seringlutut == "sering" and lutut == "sakit":
            skorlutut = 9
        elif seringlutut == "sering" and lutut == "sakit parah":
            skorlutut = 12
        elif seringlutut == "selalu" and lutut == "tidak ada masalah":
            skorlutut = 4
        elif seringlutut == "selalu" and lutut == "tidak nyaman":
            skorlutut = 8
        elif seringlutut == "selalu" and lutut == "sakit":
            skorlutut = 12
        elif seringlutut == "selalu" and lutut == "sakit parah":
            skorlutut = 16
        else:
            skorlutut = 0

        if skorlutut < 2:
            nilailutut = "aman"
        elif skorlutut < 7:
            nilailutut = "perlu pengamatan lebih lanjut"
        else:
            nilailutut = "bahaya"

        # betis
        if seringbetis == "tidak pernah" and betis == "tidak ada masalah":
            skorbetis = 1
        elif seringbetis == "tidak pernah" and betis == "tidak nyaman":
            skorbetis = 2
        elif seringbetis == "tidak pernah" and betis == "sakit":
            skorbetis = 3
        elif seringbetis == "tidak pernah" and betis == "sakit parah":
            skorbetis = 4
        elif seringbetis == "terkadang" and betis == "tidak ada masalah":
            skorbetis = 2
        elif seringbetis == "terkadang" and betis == "tidak nyaman":
            skorbetis = 4
        elif seringbetis == "terkadang" and betis == "sakit":
            skorbetis = 6
        elif seringbetis == "terkadang" and betis == "sakit parah":
            skorbetis = 8
        elif seringbetis == "sering" and betis == "tidak ada masalah":
            skorbetis = 3
        elif seringbetis == "sering" and betis == "tidak nyaman":
            skorbetis = 6
        elif seringbetis == "sering" and betis == "sakit":
            skorbetis = 9
        elif seringbetis == "sering" and betis == "sakit parah":
            skorbetis = 12
        elif seringbetis == "selalu" and betis == "tidak ada masalah":
            skorbetis = 4
        elif seringbetis == "selalu" and betis == "tidak nyaman":
            skorbetis = 8
        elif seringbetis == "selalu" and betis == "sakit":
            skorbetis = 12
        elif seringbetis == "selalu" and betis == "sakit parah":
            skorbetis = 16
        else:
            skorbetis = 0

        if skorbetis < 2:
            nilaibetis = "aman"
        elif skorbetis < 7:
            nilaibetis = "perlu pengamatan lebih lanjut"
        else:
            nilaibetis = "bahaya"

        # kaki
        if seringkaki == "tidak pernah" and kaki == "tidak ada masalah":
            skorkaki = 1
        elif seringkaki == "tidak pernah" and kaki == "tidak nyaman":
            skorkaki = 2
        elif seringkaki == "tidak pernah" and kaki == "sakit":
            skorkaki = 3
        elif seringkaki == "tidak pernah" and kaki == "sakit parah":
            skorkaki = 4
        elif seringkaki == "terkadang" and kaki == "tidak ada masalah":
            skorkaki = 2
        elif seringkaki == "terkadang" and kaki == "tidak nyaman":
            skorkaki = 4
        elif seringkaki == "terkadang" and kaki == "sakit":
            skorkaki = 6
        elif seringkaki == "terkadang" and kaki == "sakit parah":
            skorkaki = 8
        elif seringkaki == "sering" and kaki == "tidak ada masalah":
            skorkaki = 3
        elif seringkaki == "sering" and kaki == "tidak nyaman":
            skorkaki = 6
        elif seringkaki == "sering" and kaki == "sakit":
            skorkaki = 9
        elif seringkaki == "sering" and kaki == "sakit parah":
            skorkaki = 12
        elif seringkaki == "selalu" and kaki == "tidak ada masalah":
            skorkaki = 4
        elif seringkaki == "selalu" and kaki == "tidak nyaman":
            skorkaki = 8
        elif seringkaki == "selalu" and kaki == "sakit":
            skorkaki = 12
        elif seringkaki == "selalu" and kaki == "sakit parah":
            skorkaki = 16
        else:
            skorkaki = 0

        if skorkaki < 2:
            nilaikaki = "aman"
        elif skorkaki < 7:
            nilaikaki = "perlu pengamatan lebih lanjut"
        else:
            nilaikaki = "bahaya"

        gotrak = Hasil(perusahaan=perusahaan, nama=nama, posisi=posisi, email=email, tugas1=tugas1, tugas2=tugas2, tugas3=tugas3, waktu1=waktu1, waktu2=waktu2, waktu3=waktu3, tgn=tgn, lama=lama, mental=mental, fisik=fisik, sakit=sakit, bagian=bagian, skorleher=skorleher, nilaileher=nilaileher, skorbahu=skorbahu, nilaibahu=nilaibahu, skorpa=skorpa, nilaipa=nilaipa, skorsiku=skorsiku,
                       nilaisiku=nilaisiku, skorpb=skorpb, nilaipb=nilaipb, skorlengan=skorlengan, nilailengan=nilailengan, skortangan=skortangan, nilaitangan=nilaitangan, skorpinggul=skorpinggul, nilaipinggul=nilaipinggul, skorpaha=skorpaha, nilaipaha=nilaipaha, skorlutut=skorlutut, nilailutut=nilailutut, skorbetis=skorbetis, nilaibetis=nilaibetis, skorkaki=skorkaki, nilaikaki=nilaikaki)
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
