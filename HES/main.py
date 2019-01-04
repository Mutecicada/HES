#-*- coding:utf-8 -*-

from flask import Flask, render_template
from HES.user import login, regist
from HES.editor import upload
from HES.DB import DataBase

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
app.config['CKEDITOR_FILE_UPLOADER'] = 'upload'

app.register_blueprint(login.loginBp)
app.register_blueprint(regist.RegistBp)
app.register_blueprint(upload.editorBp)


@app.route('/')
def index():
    url = 'index'
    return render_template('index.html', url=url)


@app.route('/language/')
def language():
    url = 'language'
    return render_template('index.html', url=url)


@app.route('/system/')
def system():
    url = 'system'
    return render_template('board.html', url=url)


@app.route('/web/')
def web():
    url = 'web'
    return render_template('index.html', url=url)


@app.route('/network/')
def network():
    url = 'network'
    return render_template('board.html', url=url)


@app.route('/algorythm/')
def algorythm():
    url = 'algorithm'
    db = DataBase()
    db.get_cur()

    db.cur.execute(
        'SELECT title FROM board'
    )

    data = db.cur.fetchall()

    return render_template('board.html', url=url, data=data)


@app.route('/board/')
def board():
    return render_template('board.html')


if __name__ == '__main__':
    app.run(debug=True)
