from flask import \
    request, render_template, Blueprint, redirect, url_for, session, flash
from DB import DataBase
from werkzeug.security import check_password_hash

loginBp = Blueprint('loginBp', __name__, url_prefix='/user')


@loginBp.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['id']
        user_pw = request.form['passwd']
        error = None

        db = DataBase()
        db.get_cur()

        db.cur.execute(
            'SELECT id,passwd FROM usr WHERE id = %s', (user_id,)
        )
        userData = db.cur.fetchone()
        db.db_close()

        if userData is None \
                or not check_password_hash(userData['passwd'], user_pw):
            error = '아이디 또는 비밀번호를 다시 확인하세요'

        if error is None:
            session['user'] = userData['id']

            return redirect(url_for('index'))

        flash(error)

    return render_template('login.html')


@loginBp.route('/logout/')
def logout():
    session.pop('user', None)

    return redirect(url_for('index'))
