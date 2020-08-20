#! /usr/bin/env python 

from flask import Flask, url_for, redirect, abort, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])

def create_task():
	if not request.json or not 'title' in request.json:
		abort(400)
	task = { 'id': tasks[-1]['id'] + 1, 'title': request.json['title'], 'description': request.json.get('description', ""), 'done': False}
	tasks.append(task)
#    	return jsonify({'task': task})
	return make_response(jsonify(task), 200)

