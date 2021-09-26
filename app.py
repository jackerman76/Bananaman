import datetime
from flask import Flask, request, redirect, render_template, url_for, jsonify, session


app = Flask(__name__)


@app.route('/')
def home():
    return ("Welcome to the home page!")

@app.route('/login')
def login():
    return ("This is where you will login...")

@app.route('/create_account')
def create_account():
    return ("This is where you will create an account...")

@app.route('/got_bananas')
def got_bananas():
    return ("Tell us more about your bananas...")

@app.route('/need_bananas')
def need_bananas():
    return ("When you need bananas, this is where you will come...")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
