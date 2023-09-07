# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request, flash, redirect
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound
from apps.home.models import Profile
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
