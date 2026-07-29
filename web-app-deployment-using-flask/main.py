"""Main module to run flask"""
from Flask_Concept import my_app
from flask import Flask, jsonify, request

my_app.run(debug=True)

