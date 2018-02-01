# pylint: disable=E1101

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config.from_object('default_config')
app.config.from_envvar('TYCHE_CONFIG')

db = SQLAlchemy(app)


@app.route("/")
def HelloWorld():
    return "Hello, cross-origin-world!"


if __name__ == '__main__':
    app.run()
