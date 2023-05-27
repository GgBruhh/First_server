from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def welcome_page():
    return 'Welcome'