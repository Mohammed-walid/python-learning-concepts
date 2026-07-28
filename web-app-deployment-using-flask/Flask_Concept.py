"""this module is from using flask to run it"""

import flask
my_app=flask.Flask(__name__)
@my_app.route("/")
def hello_world():
    return "Hello World"



