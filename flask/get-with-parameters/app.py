from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/", methods=["GET"])
def service():
    id = request.args.get('id')
    patientid = request.args.get('patientid')

    data = {'ids' : id , 'pid' : patientid}

    return json.dumps(data)



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
