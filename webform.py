# -*- coding:utf-8 -*- 

from flask_wtf import FlaskForm
from wtforms import TextAreaField, RadioField, IntegerField, SelectField, TextField, PasswordField, SubmitField, SelectMultipleField, BooleanField, FileField
from wtforms.validators import DataRequired, Required, URL

class LoginForm(FlaskForm):
    username = TextField(validators=[Required()])
    password = PasswordField(validators=[Required()])
    submit = SubmitField("Send")

class BibtexForm(FlaskForm):
    bibtex = TextAreaField(validators=[Required()])
    tags = TextField(validators=[Required()])
    description = TextAreaField(validators=[])
    pdfupload = FileField()
    pdfweb = TextField(validators=[])
    submit = SubmitField("提交")

class EditForm(FlaskForm):
    tags = TextField(validators=[Required()])
    description = TextAreaField(validators=[])
    #pdfupload = FileField()
    #pdfweb = TextField(validators=[])
    submit = SubmitField("提交")

class CSRFForm(FlaskForm):
    pass
