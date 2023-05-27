from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home_page():
    return """
    <h1>Welcome to my beginner Website</h1>
    """

@app.route('/welcome')
def welcome_page():
    return 'Welcome'

@app.route('/welcome/home')
def welcome_home():
    return 'Welcome Home'

@app.route('/welcome/back')
def welcome_back():
    return 'Welcome Back'