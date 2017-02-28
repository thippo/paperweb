# -*- coding:utf-8 -*- 

from flask import Flask, request, session, g, flash, render_template, redirect, url_for
from webform import *
from webdb import *

import bibtexparser

app = Flask(__name__)
app.config['SECRET_KEY']='xxx'

@app.context_processor
def before_web():
    bibtexform = BibtexForm()
    try:
        return dict(username=session['username'], bibtexform=bibtexform)
    except:
        return dict(username='nologin', bibtexform=bibtexform)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    csrfform = CSRFForm()
    if 'username' in session:
        return redirect(url_for("home"))
    if request.method == 'POST':
        if request.form['username'] == 'thippo' and request.form['password'] == '123':
            session['username'] = request.form['username']
            return redirect(url_for('home'))
        else:
            flash("用户名或密码错误")
    form = LoginForm()
    return render_template('index', csrfform=csrfform, form=form)

@app.route('/logout')
def logout():
    if 'username' in session:
        csrfform = CSRFForm()
        session.pop('username', None)
        return redirect(url_for("index"))

@app.route('/home/', methods=['GET', 'POST'])
@app.route('/home/<tag_now>', methods=['GET', 'POST'])
def home(tag_now=''):
    if 'username' in session:
        bibtexform = BibtexForm()
        if bibtexform.validate_on_submit():
            try:
                lin = bibtexparser.loads(bibtexform.bibtex.data).entries[0]
                lin['bibtex'] = bibtexform.bibtex.data
                lin['tags'] = list(set(bibtexform.tags.data.split(',')))
                lin['description'] = bibtexform.description.data
                insert_db(session['username'], lin)
                flash('''<div class="alert alert-success" style="margin-top:-15px;"><a href="#" class="close" data-dismiss="alert">&times;</a><p class="text-center"><strong>添加成功</strong></div>''')
            except:
                flash('''<div class="alert alert-danger" style="margin-top:-15px;"><a href="#" class="close" data-dismiss="alert">&times;</a><p class="text-center"><strong>添加失败</strong></div>''')
        return render_template('home', tag_now=tag_now, sorted_tags=get_sorted_tags(session['username']), paper_items=get_tag_papers(session['username'], tag_now), navbar=['active', ''])
    else:
        return redirect(url_for("index"))

@app.route('/paper/<_id>', methods=['GET', 'POST'])
def paper(_id):
    if 'username' in session:
        return get_paper(session['username'], _id)
        #return chaxun()

@app.route('/delete_paper/<tag_now>/<_id>', methods=['GET', 'POST'])
def delete_paper(tag_now,_id):
    if 'username' in session:
        try:
            remove_paper(session['username'], _id)
            flash('''<div class="alert alert-success" style="margin-top:-15px;"><a href="#" class="close" data-dismiss="alert">&times;</a><p class="text-center"><strong>删除成功</strong></div>''')
        except:
            flash('''<div class="alert alert-danger" style="margin-top:-15px;"><a href="#" class="close" data-dismiss="alert">&times;</a><p class="text-center"><strong>删除失败</strong></div>''')
        return redirect('/home/'+tag_now)
    else:
        return redirect(url_for("index"))

@app.route('/tags', methods=['GET', 'POST'])
def tags():
    return str(request.form.getlist('tags_list'))

@app.route('/test', methods=['GET', 'POST'])
def test():
    if 'username' in session:
        ggl ='haha'
        #return render_template('test')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
