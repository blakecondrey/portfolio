from flask import Flask,app

app = Flask(__name__)
app.config["SECRET_KEY"] = "iNeedCoffeeAlways1!"

from routing import routing

app.register_blueprint(routing, url_prefix="")

if __name__ =='__main__':
    app.run(debug=True)