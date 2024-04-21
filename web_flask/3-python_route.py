#!/usr/bin/python3
"""starts a flask web application"""

from flask import Flask, request

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
	"""returns Hello HBNB!"""
	return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
	"""returns HBNB"""
	return 'HBNB'

# define the route for '/c/<text>'
@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
	"""display "C" followed by the value of <text>,
	Replaces any underscores in <text> with slashes."""
	# Replaces underscores with spaces in the text variable
	formatted_text = text.replace('_', ' ')
	return "C {}".format(formatted_text)

# Define the route for '/python/(<text>)'
@app.route('/python', defaults ={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text):
	"""display "Python ", followed by the value of <text>,
	Replaces any underscores in <text> with slashes."""
	return "Python {}".format(formatted_text)

if __name__ == '__main__':
	# start the flask development server
	# listen on all available network interfaces (0.0.0.0) and port 5000.
	app.run(host='0.0.0.0', port=5000)
