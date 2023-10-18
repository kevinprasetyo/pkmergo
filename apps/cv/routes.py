from apps.cv import blueprint
from flask import render_template, request, flash, redirect, Response
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound
from apps import db, login_manager
from apps.cv.models import Cv
import cv2

@blueprint.route('/sit')
@login_required
def sit():
    return render_template('cv/sit.html', segment='sit')

# camera = cv2.VideoCapture(0)

# def generate_frames():
#     while True:
#         success, frame = camera.read()
#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
        
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# @blueprint.route('/video')
# def video():
#     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@blueprint.route('/samping')
def samping():
    if "status" in request.args:
        status = request.args.get('status')
        kirim = Cv(status=status)
        db.session.add(kirim)
        db.session.commit()
        return render_template('cv/samping.html', status=status)
    else:
        return render_template('cv/samping.html', segment='samping')

@blueprint.route('/samping/laporan', methods=['GET', 'POST'])
def laporan():
    status = Cv.query.all()
    return render_template('cv/laporan.html', status=status)

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

