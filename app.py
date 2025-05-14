import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/hello')
def hello():
    return 'Hi there!'

@app.route('/bye')
def bye():
    return 'See you again!'

@app.route('/hi')
def hi():
    return 'Hello there!'

if __name__ == "__main__":
    app.run()
