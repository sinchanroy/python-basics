#! /usr/bin/env python

from flask import Flask, redirect, url_for, request, jsonify

app = Flask(__name__)


@app.route('/success/<name>')
def success(name, age):
    return 'welcome %s your age is %s  ' % name % age


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        x=jsonify(request.data);
        print (x[0]);

        user = request.form['nm']
        year = request.form['ag']
        print(user, year)
        return redirect(url_for('success', name=user, age=year))
    else:
        user = request.args.get('nm')
        year = request.args.get('ag')
        print(user, year)
        return redirect(url_for('success', name=user, age=year))


if __name__ == '__main__':
    app.run(debug=True)

