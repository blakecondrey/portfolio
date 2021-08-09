from flask import Flask,app
from flask_mail import Mail, Message

from .form import ContactForm, csrf

def create_app():

    from .routing import routing

    # mail = Mail()
    app = Flask(__name__)
    app.register_blueprint(routing, url_prefix='/')
    app.config["SECRET_KEY"] = "iNeedCoffeeAlways1!"
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'condrey.blake1217@gmail.com'
    app.config['MAIL_PASSWORD'] = 'Valeria08!'
    app.config['MAIL_USE_SSL'] = True
    # csrf.init_app(app)
    # mail.init_app(app)

    return app