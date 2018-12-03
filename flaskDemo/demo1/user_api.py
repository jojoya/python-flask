from demo1.my_app import app
from demo1.user_service import *
from flask import jsonify
from flask import json


@app.route("/user/getAll")
def get_all_api():
    users = get_all_user_service()
    print("user_API")
    print(users)
    users_dict = list_to_json(users)
    print(users_dict)
    return json.dumps(users_dict)
    # return jsonify(users_dict)


def list_to_json(users):
    users_dict = []
    for user in users:
        user_dict = user.__dict__
        print("user_dict")
        print(user_dict)
        # user_json = json(user_dict)
        # print(user_json)
        users_dict.append(user_dict)
    return users_dict


if __name__ == '__main__':
    app.run()
