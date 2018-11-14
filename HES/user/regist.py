from flask import \
    Blueprint, request, render_template, redirect, url_for, flash
from HES.DB import DataBase
from werkzeug.security import generate_password_hash

RegistBp = Blueprint('RegistBp', __name__, url_prefix='/user')


@RegistBp.route('/regist/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        uId = request.form['id']
        uPw = request.form['passwd']
        code = request.form['code']
        uName = request.form['name']
        error = None

        db = DataBase()
        db.get_cur()

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
            db.cmt()
            db.db_close()

            return redirect(url_for('loginBp.login'))

        db.db_close()
        flash(error)

    return render_template('regist.html')
