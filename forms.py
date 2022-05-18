from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, ValidationError, EqualTo

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=50, min=5)])
    email = StringField('Email', validators=[DataRequired(), Email('Please enter your email address'), Length(max=100)])
    request = TextAreaField('Reason For Contact?', validators=[DataRequired(), Length(max=1000)])
    submit = SubmitField('Submit')
    
class PasswordForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=50, min=5)])
    email = StringField('Email', validators=[DataRequired(), Email('Please enter your email address'), Length(max=100)])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=50, min=5)])
    repeat_password = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password'), Length(max=50, min=5)])
    submit = SubmitField('Submit')
