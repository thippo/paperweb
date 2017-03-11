# -*- coding:utf-8 -*- 

from flask_wtf import FlaskForm
from wtforms import TextAreaField, RadioField, IntegerField, SelectField, TextField, PasswordField, SubmitField, SelectMultipleField, BooleanField, FileField, SelectField
from wtforms.validators import DataRequired, Required, URL

class LoginForm(FlaskForm):
    username = TextField(validators=[Required()])
    password = PasswordField(validators=[Required()])
    #remember = SelectField()
    submit = SubmitField("登  录")

class BibtexForm(FlaskForm):
    secret = BooleanField()
    bibtex = TextAreaField(validators=[Required()])
    tags = TextField(validators=[Required()])
    description = TextAreaField(validators=[])
    pdfupload = FileField()
    pdfweb = TextField(validators=[])
    submit = SubmitField("提交")

class EditForm(FlaskForm):
    secret = BooleanField()
    tags = TextField(validators=[Required()])
    description = TextAreaField(validators=[])
    #pdfupload = FileField()
    pdfweb = TextField(validators=[])
    submit = SubmitField("提交")

