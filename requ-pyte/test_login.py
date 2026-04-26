import pytest
import requests
from config import LOGIN_URL

@pytest.mark.parametrize("email,password,expected_status", [
    ("17201665342@163.com", "123456", 200),
    ("17263937422@163.com", "", 401),
    ("", "123456", 401),
])
def test_login(email, password, expected_status):
    payload = {
        "email": email,
        "password": password
    }

    result = requests.post(LOGIN_URL, json=payload)

    print(result.status_code)
    print(result.json())

    assert result.status_code == expected_status