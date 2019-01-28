from flask import \
    request, render_template, Blueprint, redirect, url_for, session, flash
from DB import DataBase
from werkzeug.security import check_password_hash, generate_password_hash

account = Blueprint('account', __name__, url_prefix='/user')


@account.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['id']
        user_pw = request.form['passwd']
        error = None

        db = DataBase()

        db.cur.execute(
            'SELECT id,passwd FROM usr WHERE id = %s', (user_id,)
        )
        userData = db.cur.fetchone()
        db.db.close()

        if userData is None \
                or not check_password_hash(userData['passwd'], user_pw):
            error = '아이디 또는 비밀번호를 다시 확인하세요'

        if error is None:
            session['user'] = userData['id']

            return redirect(url_for('main'))

        flash(error)

    return render_template('login.html')


@account.route('/regist/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        uId = request.form['id']
        uPw = request.form['passwd']
        code = request.form['code']
        uName = request.form['name']
        error = None

        db = DataBase()

        db.cur.execute(
            'SELECT id FROM usr WHERE id = %s', (uId,)
        )
        uData = db.cur.fetchone()

        if uData is not None:
            error = "이미 존재하는 아이디입니다"

        if error is None:
            db.cur.execute(
                'INSERT INTO usr (id, passwd, code, usr_name) VALUES (%s,%s,%s,%s)',
                (uId, generate_password_hash(uPw), code, uName)
            )
            db.db.commit()
            db.db.close()

            return redirect(url_for('account.login'))

        db.db.close()
        flash(error)

    return render_template('regist.html')


@account.route('/logout/')
def logout():
    session.pop('user', None)

    return redirect(url_for('main'))
