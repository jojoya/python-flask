import json


# lists = [1, 2, 3]
lists = [1]
# print(len(lists))
# lists.reverse()
# print(lists)
# print(tuple(lists))
print(str(tuple(lists)).replace(',', ''))
# print(str(lists)[1:len(lists)-1])
data = {}
data = '{}'
print(json.loads(data))
# data1 = {'param1': 'value1', 'param2': 'value2'}
# data2 = {'param3': 'value3', 'param4': 'value4'}
# data3 = {'param1': 1111, 'param3': '3333'}
# data = {}
# data.update(data1)
# data.update(data2)
# data.update({'data3': data3})
# print(data)
# print(json.dumps(data))
#
# null = ''
# data = {'null': null}
# print(data)
#
# obj = {}
# print(json.dumps(obj))
# print(obj.__dict__)