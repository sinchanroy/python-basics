#! /usr/bin/env python 

from flask import Flask, url_for, request, render_template, redirect
app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return 'welcome %s ' % name 



@app.route('/login', methods=['POST','GET'])
def login():
	if request.method == 'POST':
		username = request.form.get('name')
		password = request.form.get('pass')
		sex = request.form.get('gender')
		dob = request.form.get('bday')
		print(username)
		print(password)
		print(sex)
		print(dob)
		return redirect(url_for('success', name = username))

	else:
		username = request.args.get('name')
		print(username)
		return redirect(url_for('success', name = username))


if __name__ == '__main__':
    app.run(debug=True)




