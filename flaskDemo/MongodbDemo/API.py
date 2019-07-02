from flask import request, jsonify

from MongodbDemo.MongoEngineDemo01 import app
from MongodbDemo.User import Address


@app.route('/index')
def index():
    return 'Hello World!'


@app.route('/mdb_list', methods=['get'])
def mdb_list():
    name = request.args.get('name')
    address = request.args.get('address')
    Addr = Address.objects(name=name, address=address).first()

    if not Addr:
        Address(name=name, address=address).save()
        return jsonify({'code': 1, 'message': 'success'})
    else:
        return jsonify(Addr.to_json())
