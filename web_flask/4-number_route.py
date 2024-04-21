#!/usr/bin/python3
"""starts a Flask web application."""

from flask import Flask, request
app = Flask(__name__)

# Define the route for the root URL. '/'
@app.route('/', strict_slashes=False)
def hello_hbnb():
	"""Displays 'Hello HBNB!'."""
	return "Hello HBNB!"

# Define the route for '/hbnb'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
	"""displays 'HBNB'."""
	return "HBNB"
# Define the route for '/c/<text>'
@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
	"""displays 'C' followed by the value of <text>.
	Replaces any underscores in <text> with slashes."""
	# Replaces underscores with spaces in the text variable
	formatted_text = text.replace('_', ' ')
	return "C {}".format(formatted_text)

# Define the route for '/python/(<text>)'
@app.route('/python/', defaults={'text', 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text):
	"""Displays 'python' followed by the value of <text>.
	Replaces any underscores in <text> with slashes."""
	# Replace underscores with spaces in the text variable
	formatted_text = text.replace('_', ' ')
	return "python{}".format(formatted_text)

# Define the route for '/number/<n>'
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
	"""displays 'n is a number' only if n is an integer."""
	return "{} is a number".format(n)

if __name__ == "__main__":
	# start the flask development server
	#listen on all available network interface (0.0.0.0) and port 5000
	app.run(host='0.0.0.0', port=5000)
