from flask import Flask
from flask_cors import CORS
from flask import request
app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route("/")
def helloWorld():
    return "Hello, cross-origin-world!"


@app.route("/users/Register", methods=['POST', 'GET'])
def RegisterUser():
    return request.form['email']


if __name__ == '__main__':
    app.run(debug=True)
