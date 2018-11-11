from flask import (
    request, render_template, Blueprint, redirect, url_for, session, flash
)
from DB import DataBase
from werkzeug.security import check_password_hash

user = Blueprint('user', __name__)


@user.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['id']
        user_pw = request.form['passwd']
        error = None

        db = DataBase()
        db.get_cursor()

        db.cur.execute(
            'SELECT id,passwd FROM usr WHERE id = %s', (user_id,)
        )

        userData = db.cur.fetchone()

        if userData is None:
            error = '잘못된 정보입니다'
        elif not check_password_hash(userData['passwd'], user_pw):
            error = '잘못된 정보입니다'

        if error is None:
            session['user'] = userData['id']
            db.db_close()

            return redirect(url_for('index'))

        flash(error)
        db.db_close()

    return render_template('login.html')


@user.route('/logout/')
def logout():
    session.pop('user', None)

    return redirect(url_for('index'))
