import pytest
import requests
from config import LOGIN_URL

"""
全局 fixture
"""
@pytest.fixture(scope="session")
def token():
    """登录获取 token"""
    data = {
        "email": "17201665342@163.com",
        "password": "123456"
    }

    result = requests.post(LOGIN_URL, json=data)

    assert result.status_code == 200
    assert result.json()["code"] == 0

    token = result.json()["data"]["token"]
    return token