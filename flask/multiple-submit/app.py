#! /usr/bin/env python

import flask

app = flask.Flask(__name__)
app.config["DEBUG"]=True

@app.route('/invocations-documentbased', methods=['POST'])
def documentbased():
    print("Hello Document Based")

@app.route('/invocations-sentencebased', methods=['POST'])
def sentencebased():
    print("No Hello ")

app.run(0.0.0.0, port=8080)
