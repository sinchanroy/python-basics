#! /usr/bin/env python

from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
	return "hello" + name




#app.add_url_rule('/', 'hello', hello)

if __name__ == '__main__':
	app.run()




