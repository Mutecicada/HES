#-*- coding:utf-8 -*-

from flask import Flask, render_template
from user import login

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
app.register_blueprint(login.loginBp)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/language/')
def language():
    return render_template('language.html')


@app.route('/system/')
def system():
    return render_template('system.html')


@app.route('/web/')
def web():
    return render_template('web.html')


@app.route('/network/')
def network():
    return render_template('network.html')


@app.route('/algorythm/')
def algorythm():
    return render_template('algorythm.html')

@app.route('/regist/')
def regist():
    return render_template('regist.html')

if __name__ == '__main__':
    app.run(debug=True)
