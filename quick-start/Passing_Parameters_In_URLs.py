import requests
import json


"""
在 URL 中传递参数
"""
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)

payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)
print(r.encoding)   # utf-8
print(r.text)

"""
JSON 响应
"""
r = requests.get('https://api.github.com/events')
print(r.json())
print(json.dumps(r.json(), indent=2))   # 标准输出

"""
requests.post
"""
# url = 'https://httpbin.org/post'
# # 显示文件名、内容类型和标头（Content-Type：application/json）
# files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
# r = requests.post(url, files=files)
# print(r.text)

"""
响应状态码
"""
r = requests.get('https://httpbin.org/get')
print(r.status_code)    # 200

bad_r = requests.get('https://httpbin.org/status/404')
print(bad_r.status_code)    # 404
# print(bad_r.raise_for_status()) # 抛出异常

"""
获取 cookie
"""
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
print(r.cookies['example_cookie_name'])

"""
要向服务器发送您自己的 cookie
"""
url = 'https://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print(r.text)   # '{"cookies": {"cookies_are": "working"}}'