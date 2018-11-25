from app.my.my_user import User
from app.my.my_app import db


# 2.增加记录
admin = User(username='admin', email='admin@example.com')
guest = User(username='guest', email='guest@example.com')
add_result = db.session.add(admin)      # 添加一个
print("add.admin:")
print(add_result)
add_result = db.session.add(guest)      # 添加一个
print("add.guest:")
print(add_result)
add_result = db.session.add_all([admin, guest])   # 添加多个
print("add.[admin, guest]:")
print(add_result)
db.session.commit()

# 修改1
query_result = User.query.filter_by(username='admin').first()
query_result.username = 'jojoya'  # 修改方法1
db.session.commit()
query_result = User.query.filter_by(username='jojoya').update({'username': 'new_admin'})  # 修改方法2
db.session.commit()


# 3.查询记录,注意查询返回对象，如果查询不到返回None
query_result = User.query.all()    # 查询所有
print('查询所有:')
print(query_result)
User.query.filter_by(username='new_admin').update({'username': 'jojoya'})
query_result = User.query.filter_by(username='jojoya').first()  # 条件查询
print('条件查询first:')
print(query_result)
print(query_result.__dict__)
print('id='+str(query_result.id)+',username='+query_result.username+',email='+query_result.email)
query_result = User.query.order_by(User.username).all()    # 排序查询
print('排序查询:')
print(query_result)
query_result = User.query.limit(1).all()   # 查询1条
print('查询1条:')
print(query_result)
query_result = User.query.get(1)  # 精确查询
print('精确查询:')
print(query_result)
# query_result = User.query.get_or_404(1)  # 精确查询get_or_404
# print('精确查询get_or_404:')
# print(query_result)


query_result = User.query.filter_by(username='jojoya').first()  # 条件查询
print('条件查询first:')
print(query_result)


# query_result = User.query.filter_by(User.username=='guest', email='guest@example.com').first()  # 多条件查询
query_result = User.query.filter_by(username='guest', email='guest@example.com').first()  # 多条件查询
print('查询：多条件:')
print(query_result)
users_endswith = User.query.filter(User.email.endswith('@example.com')).all()
print('查询：users_endswith:')
print(users_endswith)
users_startswith = User.query.filter(User.email.startswith('admin')).all()
print('查询：users_startswith:')
print(users_startswith)
users_like = User.query.filter(User.email.like('example')).all()
print('查询：users_like:')
print(users_like)


# 4.删除
# user = User.query.get(2)
user = User.query.filter_by(username='guest').first()
db.session.delete(user)
db.session.commit()


delete_users = User.query.filter(User.email.endswith('@example.com')).all()
print('delete_users:')
print(delete_users)
for user in delete_users:
    db.session.delete(user)
db.session.commit()

# user = User.query.filter_by(username='admin').first_or_404()



