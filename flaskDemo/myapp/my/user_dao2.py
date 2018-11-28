# from sqlalchemy.sql.elements import or_, and_

from sqlalchemy import and_, or_, not_
from myapp.my.my_user import User
from myapp.my.my_app import db

# 添加数据
user = User('xiaoxiao', 'ss123', 1)
user.save()
# 按条件查询
result = User.query.filter(User.id > 5).all()
print(result)
result = User.query.filter(User.username == 'xiaoxiao').all()  # 返回结果为一个列表,列表内元素为User对象,all()为返回查询的所有结果,first()返回查询结果中的第一个
result = User.query.filter(User.username.startswith('x'))  # starstwith以什么开头
# 获取查询结果的总数量
count = User.query.filter(User.id > 5).count()
# 获取查询结果中指定的数据
result = User.query.filter(User.id > 5).all()[1:3]  # 查询结果以列表返回,所以可以根据列表的切片操作来获取对应数据
print(result)

# 多条件查询
# sqlalchemy内置了多条件查询方法 : and_(), or()_ ,not_()
result = User.query.filter(and_(User.id > 43, User.username.startswith('x'))).all()  # 查询id大于5并且用户名以x开头的
print('查询id大于5并且用户名以x开头的')
print(result)
result = User.query.filter(or_(User.id > 43, User.username.startswith('x'))).all()  # 查询id大于5或者用户名以x开头的
print('查询id大于5或者用户名以x开头的')
print(result)
result = User.query.filter(and_(User.username.startswith('x'))).all()  # 查询用户名不是以x开头的
print('查询用户名不是以x开头的')
print(result)

# 修改
result = User.query.filter(User.username == 'xiaoxiao').all()[0]
result.password = '000000'
db.session.commit()

# 删除
result = User.query.filter(User.username == 'xiaoxiao').all()[0]
db.session.delete(result)
db.session.commit()

