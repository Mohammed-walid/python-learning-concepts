"""this module is from using flask to run it"""

from flask import Flask, request, render_template

my_app=Flask(__name__)
@my_app.route("/")
def hello_world():
    """this function is to display the home page"""
    return "Hello World"

@my_app.route("/hello")
def hello():
    """this function is to display the page /hello"""
    return "Hello"

@my_app.route("/sample/")
def get_sample_html():
    return render_template("sample.html")


@my_app.route("/user/<username>", methods=["GET"])
def greet_user(username):
    return render_template("result.html", username=username)


@my_app.route("/user", methods=["GET"])
def greet_user_based_on_req():
    user_name = request.args.get("username")
    return render_template("result.html", username=user_name)

