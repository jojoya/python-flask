#!/usr/bin/env python
# -*- coding: utf-8 -*-


from MongodbDemo.MongoEngineDemo01 import mdb


# 类名定义 collection
class Users(mdb.Document):
    # 字段
    name = mdb.StringField()
    email = mdb.StringField()

    def __str__(self):
        return "name:{} - email:{}".format(self.name, self.email)


class Address(mdb.Document):
    name = mdb.StringField()
    address = mdb.StringField()

    # 查询 Address.objects(name="zhangsan").first()

    # 添加 Address(name='lisi', address='lisi@gmail.com').save()

    # 删除 Address.delete()

    # 更新 Address.update(name="lisi@outlook.com")


if __name__ == '__main__':
    # Address(name='lisi', address='lisi@gmail.com').save()
    address: Address = Address.objects(name="lisi").first()

    print(address._data)
    print(str(address.id))
    print(type(address.id))
    print(address.to_json())
    print(address.to_mongo())
    # Address.delete()