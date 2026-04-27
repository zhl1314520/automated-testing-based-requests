import pytest
import requests
from config import LOGIN_URL

"""
全局 fixture
"""
@pytest.fixture(scope="session")
def token():
    """获取稳定的登录 token """
    data = {
        "email": "17201665342@163.com",
        "password": "123456"
    }   # 依赖登录结果

    result = requests.post(LOGIN_URL, json=data)

    assert result.status_code == 200

    token = result.json()["token"]
    return token