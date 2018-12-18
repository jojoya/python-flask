import json

from websocketDemo4.main import main


class ServiceCheckApi(object):
    @main.route('/list', methods=['POST'])
    def get_list(self, data):
        return json.jsonfiy(data)


class GetRecordData(object):
    @main.route('/get/<ids>', methods=['GET'])
    def get_ids(self, ids):
        return json.jsonfiy({'ids': ids})
