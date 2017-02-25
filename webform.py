from flask_wtf import Form
from wtforms import TextAreaField, RadioField, IntegerField, SelectField, TextField, SubmitField
from wtforms.validators import DataRequired, Required

class BibtexForm(Form):
    bibtex = TextAreaField(validators=[Required()])
    tags = TextField(validators=[Required()])
    description = TextAreaField(validators=[Required()])
    submit = SubmitField("Send")
