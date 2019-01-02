from flask import \
    Blueprint, render_template, request, redirect
from HES.DB import DataBase

editorBp = Blueprint('editorBp', __name__, url_prefix='/post')

url = None


@editorBp.route('/editor/', methods=['GET', 'POST'])
def editor():
    global url

    if request.headers['Referer'].find('/post/editor/') == -1:
        url = request.headers['Referer']

    if request.method == 'POST':
        title = request.form['title']
        post = request.form['post']

        db = DataBase()
        db.get_cur()

        db.cur.execute(
            'INSERT INTO board(title,post) VALUES (%s, %s)',
            (title, post)
        )
        db.cmt()
        db.db_close()

        return redirect(url)
    else:
        return render_template('editor.html')
