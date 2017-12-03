#Main Python page using flask framework

import flask as fl
from flask import render_template, request# imports the render template property which allows html pages be loaded as the template for the pages on the server
from werkzeug.utils import secure_filename
app = fl.Flask(__name__)

@app.route("/")
def name():
    return render_template('Main.html')

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if __name__ == "__main__":
    app.run() # runs the app