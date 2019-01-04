from flask import \
    Blueprint, render_template, request, redirect, current_app, url_for
from HES.DB import DataBase
import os
import json
import datetime


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


@editorBp.route('/editor/upload/', methods=['GET', 'POST'])
def upload():
    error = ''
    url = ''
    callback = request.args.get('CKEditorFuncNum')

    if request.method == 'POST' and 'upload' in request.files:
        f = request.files['upload']
        fname, fext = os.path.splitext(f.filename)
        rnd_name = '%s%s' % (datetime.datetime.now().strftime('%Y%m%d%H%M%S'), fext)
        filepath = os.path.join(current_app.static_folder, 'upload', rnd_name)
        dirname = os.path.dirname(filepath)

        if not os.path.exists(dirname):
            try:
                os.makedirs(dirname)
            except:
                error = 'ERROR_CREATE_DIR'
        elif not os.access(dirname, os.W_OK):
            error = 'ERROR_DIR_NOT_WRITEABLE'

        if not error:
            f.save(filepath)
            url = url_for('static', filename='%s%s' % ('upload/', rnd_name))
    else:
        error = 'post error'

    res = {"uploaded": 1, "filename": "%s" % rnd_name, "url": "%s" % url}
    res = json.dumps(res)

    return res
