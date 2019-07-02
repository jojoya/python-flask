import requests
import socket
from requests import request


def cres_print(res):
    print('url-----------------------')
    print(res.url)
    print('request-----------------------')
    print(res.request)
    print('headers-----------------------')
    print(res.headers)
    print('cookies-----------------------')
    print(res.cookies)
    print('text响应正文-----------------------')
    print(res.text)
    print('json响应正文-----------------------')
    print(res.json)
    print('status_code-----------------------')
    print(res.status_code)
    print('reason-----------------------')
    print(res.reason)
    print('encoding-----------------------')
    print(res.encoding)


def getIP(domain):
    """
    查看域名DNS映射
    :param domain:
    :return:
    """
    myaddr = socket.getaddrinfo(domain, 'https')
    print(myaddr[0][4][0])


# getIP('www.workec.com')


headers = {'Host': '10.0.201.174'}
params = {'key1': '${param1}', 'key2': 'param2'}

url = "https://www.workec.com"
res = requests.get(url=url, headers=headers, params=params)
print(res.request.__dict__)
# print(res.raw._connection.sock.getpeername()[0])
# print(res.raw._connection.sock.getsockname()[0])
cres_print(res)


# url = "https://www.workec.com/default/statistics"
# res = requests.post(url=url, headers=headers, proxies=proxy).content.decode()
# # res = request(method='POST', url=url, proxies=proxy)
# cres_print(res)

# ec_cookies = res.cookies
# ec_csrf_token = res.cookies['ec_csrf_token']

# url = "https://biz.workec.com/auth"
# headers = {'ec_csrf_token': ec_csrf_token, 'X-Requested-With': 'XMLHttpRequest'}
# # res = requests.get(url, params=params, headers=headers)
# res = request(method='GET', url=url, headers=headers, cookies=ec_cookies, timeout=1)
# cres_print(res)


"""post json-data"""
# headers = {'Content-Type': 'multipart/form-data'}
# headers = {'Content-Type': 'application/x-www-form-urlencoded'}
# headers = {'Content-Type': 'application/json'}
# url = "https://open.workec.com/auth/accesstoken"
# json = {'appId': 200307256498061312, 'appSecret': 'm1lSYLQOcKh08KxmjaN'}
# res = requests.post(url, json=json, headers=headers)
# res = request(method='POST', url=url, json=json, headers=headers)
# cres_print(res)

"""post form-data"""
# headers = {'Content-Type': 'application/x-www-form-urlencoded'}
# url = 'http://10.0.201.197:3000/api/tester/encrypt'
# data = {'str': '{"account": 14422222222,"password": "a88888","step": "1"}'}
# # res = requests.post(url, headers=headers, data=data)
# res = request(method='POST', url=url, headers=headers, data=data)
# cres_print(res)

