# pylint: disable=E0401
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from route import rule

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config.from_object('default_config')
app.config.from_envvar('TYCHE_CONFIG')

db = SQLAlchemy(app)


@app.route("/")
def HelloWorld():
    return "Hello, tyche-world!"


if __name__ == '__main__':
    app.register_blueprint(rule,url_prefix='/rule')
    app.run()
