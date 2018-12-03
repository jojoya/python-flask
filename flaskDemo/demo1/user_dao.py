from demo1.user_model import User
from demo1.my_app import db

user1 = User("name1", "email1@qq.com")
user2 = User("name2", "email2@qq.com")


# 查询
def get_all_user_dao():
    dao_users = User.query.all()
    print("dao_users")
    print(dao_users)
    return dao_users


def get_one_by_id(id):
    return User.query.get(id)


def get_first_by_name(username):
    return User.query.filter_by(username=username).first()


def get_all_by_name(username):
    return User.query.filter_by(username=username).all()


# 修改
def update_first_by_name(name):
    user = get_first_by_name(name)
    email = user.email
    end = email[email.find("@"):]
    start = user.username
    user.email = start + end
    db.session.commit()


def update_email_by_name(name, email):
    user = get_first_by_name(name)
    end = user.email[user.email.find("@"):]
    user.email = email + end
    db.session.commit()

# 添加
def add_user(user):
    db.session.add(user)
    db.session.commit()


# 删除
def del_user(user):
    db.session.delete(user)
    db.session.commit()


def del_firt_user_by_name(name):
    user = get_first_by_name(name)
    del_user(user)


def del_all_user_by_name(name):
    del_users = get_all_by_name(name)
    for user in del_users:
        del_user(user)


if __name__ == '__main__':
    i = 0
    while i < 5:
        name = "JoJoYo" + str(i)
        email = name + "@qq.com"
        user = User(name, email)
        import json
        # print(json.dumps(user.__dict__))
        add_user(user)
        i += 1
    # db.session.commit()
    # add_user(user1)
    # add_user(user2)
    # print(get_all_user_dao())
    # print(get_all_user_dao()[0].__dict__)
    #
    # update_first_by_name("name1")
    # update_email_by_name("name2", "jojoya")
    #
    # # print(get_one_by_id(60))
    # # print(get_one_by_id(60).__dict__)
    # print(get_first_by_name(username="name1"))
    # print(get_first_by_name(username="name1").__dict__)
    # print(get_all_by_name(username="name2"))
    # print(get_all_by_name(username="name2")[0].__dict__)
    #
    # del_firt_user_by_name("name1")
    # del_all_user_by_name("name1")
    # del_all_user_by_name("name2")
