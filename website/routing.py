from os import abort
from flask import Blueprint, render_template, request, flash, current_app
from flask_mail import Message, Mail
from .form import ContactForm

contact_points = {
    "email": "condrey.blake1217@gmail.com",
    "github": "https://github.com/blakecondrey",
    "linkedin": "https://www.linkedin.com/in/blakecondrey/",
    "crwnfit": "http://crwnfit.herokuapp.com/",
    "newsagg": "https://blakecondreynewsagg.herokuapp.com/",
    "algo": "https://blakecondrey.github.io/sortingvisualizer/"
}

routing = Blueprint("routing", __name__, static_folder="static", template_folder="templates")

def send_email(result):
    msg = Message(sender = result.get('email'),
    recipients = ['condrey.blake1217@gmail.com'])
    msg.body = """
    Hello there,

    You just received a contact form.

    Name: {}
    Email: {}
    Message: {}
    """.format(result['name'], result['email'], result['message'])
    mail = Mail()
    mail.init_app(current_app)
    mail.send(msg)

@routing.route("/")
def home():
    return render_template("home.html", contact=contact_points)

@routing.route('/projects')
def projects():
    return render_template("projects.html", contact=contact_points)

@routing.route("/contact/", methods=['GET', 'POST'])
def contact():
    name = None
    email = None
    subject = None
    message = None
    form = ContactForm()
    if request.method == 'POST':
        result = {}
        result['name'] = request.form['name']
        result['email'] = request.form['email'].replace(' ', '').lower()
        result['subject'] = request.form['subject']
        result['message'] = request.form['message']
        send_email(result)
        return render_template("contact.html", contacts=contact_points, success=True)

    elif request.method == 'GET':
        return render_template("contact.html", contacts=contact_points, form = form)
