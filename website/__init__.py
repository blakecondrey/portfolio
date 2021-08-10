from flask import Flask,app
from flask_mail import Mail, Message


def create_app():

    from .routing import routing

    app = Flask(__name__)
    app.register_blueprint(routing, url_prefix='/')
    app.config["SECRET_KEY"] = "iNeedCoffeeAlways1!"
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_SSL'] = True

    return app
