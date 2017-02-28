# -*- coding:utf-8 -*- 

from flask_wtf import Form
from wtforms import TextAreaField, RadioField, IntegerField, SelectField, TextField, PasswordField, SubmitField, SelectMultipleField, BooleanField
from wtforms.validators import DataRequired, Required

class LoginForm(Form):
    username = TextField(validators=[Required()])
    password = PasswordField(validators=[Required()])
    submit = SubmitField("Send")

class BibtexForm(Form):
    bibtex = TextAreaField(validators=[Required()])
    tags = TextField(validators=[Required()])
    description = TextAreaField(validators=[])
    submit = SubmitField("提交")

class CSRFForm(Form):
    pass
