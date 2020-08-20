#! /usr/bin/env python

from flask import Flask, url_for, redirect
app = Flask(__name__)

@app.route('/admin')
def admin():
	return "Hello Admin"

@app.route('/guest/<guest>')
def guest(guest):
	return "Guest %s " % guest

@app.route('/user/<name>')
def user(name):
	if name == 'admin':
		return redirect(url_for('admin'))
	else:
		return redirect(url_for('guest', guest = name))

if __name__ == '__main__':
   app.run(debug = True)
