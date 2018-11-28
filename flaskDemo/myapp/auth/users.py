from flask import request, jsonify
from myapp.models import *
from myapp.auth.__init__ import auth


@auth.route('/apidemo', methods=['GET', 'POST'])
def apidemo():
    """一个返回JSON数据接口的设计示例"""

    jsonResponse = dict(errCode="1", errMsg="操作成功！")
    response = jsonify(jsonResponse)
    return response
