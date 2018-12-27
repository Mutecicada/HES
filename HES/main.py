#-*- coding:utf-8 -*-

from flask import Flask, render_template
from HES.user import login, regist

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
app.register_blueprint(login.loginBp)
app.register_blueprint(regist.RegistBp)


@app.route('/')
def index():
    url = 'index'
    return render_template('index.html',url=url)


@app.route('/editor/')
def editor():
    return render_template('editor.html')


@app.route('/language/')
def language():
    url = 'language'
    return render_template('index.html',url=url)


@app.route('/system/')
def system():
    url = 'system'
    return render_template('board.html',url=url)


@app.route('/web/')
def web():
    url = 'web'
    return render_template('index.html',url=url)


@app.route('/network/')
def network():
    url = 'network'
    return render_template('board.html',url=url)


@app.route('/algorythm/')
def algorythm():
    url = 'algorithm'
    return render_template('board.html',url=url)

@app.route('/board/')
def board():
    return render_template('board.html')

if __name__ == '__main__':
    app.run(debug=True)
