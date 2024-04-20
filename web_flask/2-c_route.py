#!/usr/bin/python3
""" starts a flash web application C is FUN """

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
	""" displays 'Hello HBNB!' """
	return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
	""" displays 'HBNB' """
	return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
	""" Displays 'C' followed by the value of <text>. """
	# Replace underscores with spaces in the text variables
	formatted_text = text.replace('_', ' ')
	return "C ()".format(formatted_text)

if __name__ == "__main__":
	# start the flask development server
	# listen on all available network interface (0.0.0.0) and port 5000
	app.run(host='0.0.0.0', port=5000)
