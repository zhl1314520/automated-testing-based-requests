import requests


s = requests.Session()

s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('https://httpbin.org/cookies')

print(r.text)   # 服务端返回的 cookie（session_id） 信息

"""
获取服务器返回的 HTTP 请求头
"""
r = requests.get('https://en.wikipedia.org/wiki/Monty_Python')
print(r.headers)
"""
获取发送给服务器的 HTTP 请求头
"""
print(r.request.headers)