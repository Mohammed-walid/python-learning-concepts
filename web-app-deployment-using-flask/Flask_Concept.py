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

