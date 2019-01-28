#-*- coding:utf-8 -*-

from flask import Flask, render_template
from user import login, regist
from editor import upload
from DB import DataBase

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
app.config['CKEDITOR_FILE_UPLOADER'] = 'upload'

app.register_blueprint(login.loginBp)
app.register_blueprint(regist.RegistBp)
app.register_blueprint(upload.editorBp)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/<category>/')
def index(category):
    con1 = ['language', 'web']
    if category in con1:
        print('url ok')
        return render_template('index.html', url=category)
    else:
        db = DataBase()
        db.get_cur()

        db.cur.execute(
            'SELECT * FROM board WHERE category = %s', (category,)
        )

        data = db.cur.fetchall()

        return render_template('board.html', url=category, data=data)


if __name__ == '__main__':
    app.run(debug=True)
