import requests

# 登录获取 token
login_response = requests.post("http://localhost:8000/auth/login", json={
    "email": "13637216311@163.com",
    "password": "123123"
})
token = login_response.json()["token"]
print(token)



# 使用 token 访问 /auth/me
headers = {
    "Authorization": f"Bearer {token}"
}
me_response = requests.get("http://localhost:8000/auth/me", headers=headers)
print(me_response.json())