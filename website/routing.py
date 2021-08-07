from os import abort
from flask import Blueprint, render_template, request, flash, current_app
from .form import ContactForm

contact_points = {
    "email": "condrey.blake1217@gmail.com",
    "github": "https://github.com/blakecondrey",
    "linkedin": "https://www.linkedin.com/in/blakecondrey/"
}

routing = Blueprint("routing", __name__, static_folder="static", template_folder="templates")

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
        name = form.name.data 
        email = form.email.data
        subject = form.subject.data
        message = form.message.data
        return render_template("contact.html", contacts=contact_points, success=True)

    elif request.method == 'GET':
        return render_template("contact.html", contacts=contact_points, form = form)