
def url_splicer(url, dict_params):
    if dict_params:
        url = url + '?'
        for k, v in dict_params.items():
            url = url + k + '=' + v + '&'
        url = url[:len(url)-1]
    print(url)
    return url

# dicts = {'key1': 'value1', 'key2': 'value2'}
dicts = ''
url = 'http://www.baidu.com'
url_splicer(url, dicts)