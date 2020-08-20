#! /usr/bin/env python

from flask import Flask
app = Flask(__name__)
	
@app.route('/int/<int:postID>')
def blog(postID):
	return "Blog %d" %postID

@app.route('/float/<float:revNo>')
def rev(revNo):
	return "Revision %f " %revNo

if __name__ == '__main__':
	app.run(debug=True)
