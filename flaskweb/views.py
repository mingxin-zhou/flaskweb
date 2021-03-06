from flask import Blueprint, render_template, redirect
from flask_login import login_required, current_user


bp = Blueprint("main", "main", url_prefix="/main")


@bp.route('/')
def index():
    return render_template('main.html')


@bp.route('/user')
@login_required
def user():
    return 'hello world %s' % current_user.username


@bp.route('/doc')
@login_required
def doc():
    return redirect("/swagger")
