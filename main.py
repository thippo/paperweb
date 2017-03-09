# -*- coding:utf-8 -*- 

from flask import Flask, request, session, g, make_response, flash, render_template, redirect, url_for, jsonify
from webform import *
from logindb import *
from paperdb import *
from jj2template import *

import os
from datetime import datetime
import hashlib

import bibtexparser

app = Flask(__name__)
app.config['SECRET_KEY']='xxx'

@app.before_request
def make_session_permanent():
    session.permanent = True

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
    if 'username' in session:
        return redirect(url_for('papers', who=session['username']))
    form = LoginForm()
    if form.validate_on_submit():
        if confirm_user(form.username.data, form.password.data):
            session['username'] = form.username.data
            return redirect(url_for('papers', who=session['username']))
        else:
            flash('<font color="red">用户名或密码错误</font>')
    return render_template('index', form=form)

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)
        return redirect(url_for("index"))

@app.route('/papers/<who>/', methods=['GET', 'POST'])
@app.route('/papers/<who>/<tag_now>', methods=['GET', 'POST'])
def papers(who, tag_now=''):
    if session['username'] == who:
        bibtexform = BibtexForm()
        if bibtexform.validate_on_submit():
            if 1:
            #try:
                lin = bibtexparser.loads(bibtexform.bibtex.data).entries[0]
                lin['bibtex'] = bibtexform.bibtex.data
                lin['tags'] = list(set(bibtexform.tags.data.split(',')))
                lin['description'] = bibtexform.description.data
                pdffile = bibtexform.pdfupload.data
                if pdffile:
                    lin['pdfupload'] = save_pdf_file(pdffile)
                lin['pdfweb'] = bibtexform.pdfweb.data
                lin['date'] = datetime.now()
                insert_db(session['username'], lin)
                flash(alert_div("success", "添加成功"))
            else:
            #except:
                flash(alert_div("danger", "添加失败"))
            flash(alert_div("warning", "填写有误"))
        all_papers_count = get_tag_papers_count(session['username'], tag_now)
        totalPages = all_papers_count//5+(1 if all_papers_count%5 else 0)
        return render_template('papers', tag_now=tag_now, totalPages=totalPages, sorted_tags=get_sorted_tags(session['username']), navbar=['active', ''])
    else:
        return redirect(url_for("index"))

@app.route('/showpaper/<who>/<_id>', methods=['GET', 'POST'])
def showpaper(who, _id):
    if session['username'] == who:
        paper_dict = collections.OrderedDict(get_paper(session['username'], _id))
        return render_template('showpaper', paper_dict=paper_dict)
    else:
        return redirect(url_for("index"))

@app.route('/editpaper/<who>/<_id>', methods=['GET', 'POST'])
def editpaper(who, _id):
    if session['username'] == who:
        paper_dict = collections.OrderedDict(get_paper(session['username'], _id))
        editform = EditForm(tags=','.join(paper_dict['tags']), description=paper_dict['description'])
        return render_template('editpaper', editform=editform, paper_dict=paper_dict)
    else:
        return redirect(url_for("index"))

@app.route('/updatepaper/<who>/<_id>', methods=['GET', 'POST'])
def updatepaper(who, _id):
    if session['username'] == who:
        editform = EditForm()
        if editform.validate_on_submit():
            try:
                update_paper(session['username'], _id, editform.description.data, editform.tags.data.split(','))
                flash(alert_div("success", "修改成功"))
            except:
                flash(alert_div("danger", "修改失败"))
        else:
            flash(alert_div("warning", "填写有误"))
        return redirect(url_for('papers', who=session['username']))
    else:
        return redirect(url_for("index"))

@app.route('/deletepaper/<who>/<_id>/', methods=['GET', 'POST'])
@app.route('/deletepaper/<who>/<_id>/<tag_now>', methods=['GET', 'POST'])
def deletepaper(who, _id, tag_now=''):
    if session['username'] == who:
        try:
            remove_paper(session['username'], _id)
            flash(alert_div("success", "删除成功"))
        except:
            flash(alert_div("danger", "删除失败"))
        return redirect(url_for('papers', who=session['username'], tag_now=tag_now))
    else:
        return redirect(url_for("index"))

@app.route('/downloadbibtex/<who>/<_id>')
def downloadbibtex(who, _id):
    if session['username'] == who:
        content = get_bibtex(session['username'], _id)['bibtex']
        response = make_response(content)
        response.headers["Content-Disposition"] = "attachment; filename=scholar.bib"
        return response
    else:
        return redirect(url_for("index"))

@app.route('/test', methods=['GET', 'POST'])
def test():
    if 'username' in session:
        bibtexform = BibtexForm()
        a = getone(session['username'])
        return render_template('test', a=a)

#ajax

@app.route('/ajaxtagpapers', methods=['POST'])
def ajaxtagpapers():
    if 'username' in session:
        if request.method == 'POST':
            paper_items = get_tag_pagination_papers(session['username'], request.form.get('tag', ''), request.form['pagenow'])
            data = jj2papers(session['username'], paper_items)
            return jsonify({'resultdata':data})

if __name__ == '__main__':
    app.run(debug=True)
