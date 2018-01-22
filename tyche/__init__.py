from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config.from_object('default_config')
app.config.from_envvar('TYCHE_CONFIG')

db = SQLAlchemy(app)


@app.route("/")
def helloWorld():
    return "Hello, cross-origin-world!"


@app.route("/users/Register", methods=['POST', 'GET'])
def RegisterUser():
    return request.form['email']


if __name__ == '__main__':
    app.run()
