from flask import Flask,app

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "iNeedCoffeeAlways1!"

    from .routing import routing

    app.register_blueprint(routing, url_prefix='/')

    return app