# Emerging-Tech-Project
This is my repository for my project in my Emerging Technologies module in college. 
The brief is as follows:
## brief overview
In this project you will create a web application in Python to recognise digits in images. Users will be able to visit the web application through their browser, submit (or draw) an image containing a single digit, and the web application will respond with the digit contained in the image. You should use tensorflow and flask to do this. Note that accuracy of approximately 99% is considered excellent in recognising digits, so it is okay if your algorithm gets it wrong sometimes.
## Instructions given
1. Create a git repository with a README.md and an appropriate gitignore file. The README should explain who you are, why you created the application, how you created it, how to download and run it, and summarise any references you have used.
2. In the repository, create a web application that serves a HTML page as the root resource. The page should contain an input where the user can upload (or draw) an image containing a digit, and an area to display the image and the digit.
3. Add a route to your application that accepts requests containing a user input image and responds with the digit.
4. Connect the HTML page to the route using AJAX.
brief taken from Emerging Technologies [Project Repository](https://emerging-technologies.github.io/problems/project.html)

# Technologies/Architecture
[Tensorflow](https://www.tensorflow.org/) is an open source software library for numerical computation using data flow graphs. Nodes in the graph represent mathematical operations, while the graph edges represent the multidimensional data arrays (tensors) communicated between them. The flexible architecture allows you to deploy computation to one or more CPUs or GPUs in a desktop, server, or mobile device with a single API. TensorFlow was originally developed by researchers and engineers working on the Google Brain Team within Google's Machine Intelligence research organization for the purposes of conducting machine learning and deep neural networks research, but the system is general enough to be applicable in a wide variety of other domains as well.

[Flask](http://flask.pocoo.org/)  is a micro web framework written in Python and based on the Werkzeug toolkit and Jinja2 template engine. It is BSD licensed. The latest stable version of Flask is 0.12.2 as of May 2017. Applications that use the Flask framework include Pinterest, LinkedIn, and the community web page for Flask itself. Flask is called a micro framework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools. Extensions are updated far more regularly than the core Flask program.

The famous [MNIST](http://yann.lecun.com/exdb/mnist/) data set. The MNIST database of handwritten digits, available from this page, has a training set of 60,000 examples, and a test set of 10,000 examples. It is a subset of a larger set available from NIST. The digits have been size-normalized and centered in a fixed-size image.



# How to Run
1. Download zip file from my github.
2. Unzip the folder in your prefered workspace.
3. Open some form of command line be it [command prompt](https://www.lifewire.com/command-prompt-2625840) on microsoft devices, [cmdr](http://cmder.net/), [Terminal](https://www.macworld.co.uk/feature/mac-software/how-use-terminal-on-mac-3608274/) on apple devices, or [anaconda prompt](https://anaconda.org/anaconda/python)
4. In your instance of command line navigate into the directory where you unzipped the folder.
5. To run the command "python Main.py" it will launch the html page in your browser.
6. The html page will run on your local host  http://127.0.0.1:5000/.
# Requirements for running
1. Installed instance of Python
2. Anaconda installed
3. Tensor flow installed
4. Flask Installed
# References 
[Tensorflow Tutorial](https://www.tensorflow.org/get_started/mnist/beginners)

[Flask tutorial](http://flask.pocoo.org/docs/0.12/)

[Canvas](https://www.w3schools.com/html/html5_canvas.asp)

[Basic bootstrap](https://www.w3schools.com/bootstrap/default.asp)
