from demo1.user_dao import *


def get_all_user_service():
    service_users = get_all_user_dao()
    print("service_users")
    print(service_users)
    return service_users
