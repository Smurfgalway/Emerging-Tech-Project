#Main Python page using flask framework

import flask as fl
from flask import render_template, request# imports the render template property which allows html pages be loaded as the template for the pages on the server

app = fl.Flask(__name__)

@app.route("/")
def name():
    return render_template('Main.html')


if __name__ == "__main__":
    app.run() # runs the app