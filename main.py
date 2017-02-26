# -*- coding:utf-8 -*- 

from flask import Flask, request, session, g, flash, render_template, redirect, url_for
from webform import *
from webdb import *

import bibtexparser

app = Flask(__name__)
app.config['SECRET_KEY']='xxx'

@app.context_processor
def before_web():
    try:
        return dict(username=session['username'])
    except:
        return dict(username='nologin')

@app.route('/', methods=['GET', 'POST'])
def index():
    #form = LoginForm(csrf_enabled=False)
    if 'username' in session:
        return redirect(url_for("home"))
    if request.method == 'POST':
        if request.form['username'] == 'thippo' and request.form['password'] == 'thman':
            session['username'] = request.form['username']
            return redirect(url_for('home'))
        else:
            flash("用户名或密码错误")
    form = LoginForm(csrf_enabled=False)
    return render_template('index', form=form)

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)
        return redirect(url_for("index"))

@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'username' in session:
        form = BibtexForm(csrf_enabled=False)
        return render_template('home', form=form, sorted_tags=get_sorted_tags(session['username']), titles=get_titles(session['username']))
    else:
        return redirect(url_for("index"))

@app.route('/show', methods=['GET', 'POST'])
def show():
    if 'username' in session:
        #form = BibtexForm()
        form = BibtexForm(csrf_enabled=False)
        if form.validate_on_submit():
            lin = bibtexparser.loads(form.bibtex.data).entries[0]
            lin['tags'] = list(set(form.tags.data.split(',')))
            lin['description'] = form.description.data
            insert_db(session['username'], lin)
            return 'ok'
        else:
            return 'no'

@app.route('/paper/<_id>', methods=['GET', 'POST'])
def paper(_id):
    if 'username' in session:
        return get_paper(session['username'], _id)
        #return chaxun()

@app.route('/tags/<_tag>', methods=['GET', 'POST'])
def tags(_tag):
    if 'username' in session:
        return get_tag_papers(session['username'], [_tag])

@app.route('/test', methods=['GET', 'POST'])
def test():
    if 'username' in session:
        return get_all(session['username'])

if __name__ == '__main__':
    app.run(debug=True)
