from flask import Flask, render_template
from webform import *
from webdb import *

import bibtexparser

app = Flask(__name__)
#app.config['SECRET_KEY']='xxx'

@app.route('/', methods=['GET', 'POST'])
def index():
    #form = BibtexForm()
    form = BibtexForm(csrf_enabled=False)
    return '<a href=/addpaper>add</a>'

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home', sorted_tags=get_sorted_tags(), titles=get_titles())

@app.route('/addpaper', methods=['GET', 'POST'])
def addpaper():
    #form = BibtexForm()
    form = BibtexForm(csrf_enabled=False)
    return render_template('addpaper', form=form)

@app.route('/show', methods=['GET', 'POST'])
def show():
    #form = BibtexForm()
    form = BibtexForm(csrf_enabled=False)
    if form.validate_on_submit():
        lin = bibtexparser.loads(form.bibtex.data).entries[0]
        lin['tags'] = list(set(form.tags.data.split(',')))
        lin['description'] = form.description.data
        insert_db(lin)
        return 'ok'
    else:
        return 'no'

@app.route('/paper/<_id>', methods=['GET', 'POST'])
def paper(_id):
    return get_paper(_id)
    #return chaxun()

@app.route('/tags/<_tag>', methods=['GET', 'POST'])
def tags(_tag):
    return get_tag_papers([_tag])

@app.route('/test', methods=['GET', 'POST'])
def test():
    return get_all()

if __name__ == '__main__':
    app.run(debug=True)
