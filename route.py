from flask import Flask, request, jsonify
from flask_api import status
from flasgger import Swagger
from flasgger.utils import swag_from
import api

app = Flask(__name__)
app.config['SWAGGER'] = {
    "swagger_version": "2.0",
    "title": 'Calculator',
    "specs": [
        {
            "version": "0.0.1",
            "title": "Calculator API",
            "description": "This is the draft version of Calculator API",
            "endpoint": "v1_spec",
            "route": "/v1/spec",
        }
    ]
}

Swagger(app)

def validate_and_do(callback):
    request_json = request.get_json()
    if request_json is not None and 'first' in request_json and 'second' in request_json:
        return jsonify({'result': callback(request_json['first'], request_json['second'])})
    return '', status.HTTP_400_BAD_REQUEST


@app.route('/add', methods=['POST'])
@swag_from('add.yml')
def do_add():
    return validate_and_do(api.add)


@app.route('/substract', methods=['POST'])
@swag_from('substract.yml')
def do_substract():
    return validate_and_do(api.subtract)


@app.route('/multiply', methods=['POST'])
@swag_from('multiply.yml')
def do_multiply():
    return validate_and_do(api.multiply)


@app.route('/divide', methods=['POST'])
@swag_from('divide.yml')
def do_divide():
    return validate_and_do(api.divide)


if __name__ == '__main__':
    app.run(port=5002)
