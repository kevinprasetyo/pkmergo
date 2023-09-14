from apps.cv import blueprint
from flask import render_template, request, flash, redirect
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound
from apps import db, login_manager

@blueprint.route('/cv')
@login_required
def cv():
    return "Hello World"

@blueprint.route('/sit')
@login_required
def sit():
    return render_template('cv/sit.html', segment='cv')

# Errors


@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('home/page-403.html'), 403


@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('home/page-403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('home/page-404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('home/page-500.html'), 500

