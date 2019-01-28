#-*- coding:utf-8 -*-

from flask import Flask, render_template
from account import account
from editor import upload
from DB import DataBase

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
app.config['CKEDITOR_FILE_UPLOADER'] = 'upload'

app.register_blueprint(account.account)
app.register_blueprint(upload.editorBp)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/<category>/')
def index(category):
    con1 = ['language', 'web']
    if category in con1:
        return render_template('index.html', url=category)
    else:
        db = DataBase()

        db.cur.execute(
            'SELECT * FROM board WHERE category = %s', (category,)
        )

        data = db.cur.fetchall()

        return render_template('board.html', url=category, data=data)


if __name__ == '__main__':
    app.run(debug=True)
