from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# create a form class

csrf = CSRFProtect()

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email Address", validators=[DataRequired()])
    subject = StringField("Subject", validators=[DataRequired()])
    message = StringField("Message", validators=[DataRequired()])
    send = SubmitField("Send")
