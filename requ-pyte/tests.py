import pytest
import requests
from Tools.scripts.generate_opcode_h import header

from config import LOGIN_URL, USER_INFO, USER_MANAGE, SEND_CODE, VERIFY_CODE, RESET_PASSWORD, PROJECTS_MANAGE

@pytest.mark.parametrize("email,password,expected_status", [
    ("17201665342@163.com", "123456", 200),
    ("17263937422@163.com", "", 401),
    ("", "123456", 401),
])
def test_login(email, password, expected_status):
    # 登录接口本身
    payload = { # payload 本质上是一个请求体
        "email": email,
        "password": password
    }

    result = requests.post(LOGIN_URL, json=payload)

    print(result.status_code)
    print(result.json())

    assert result.status_code == expected_status


@pytest.mark.parametrize("expected_status", [
    200
])
def test_user_info(token, expected_status):
    result = requests.get(USER_INFO, headers={"Authorization": f"Bearer {token}"})
    print(result.status_code)
    print(result.json())

    assert result.status_code == expected_status


@pytest.mark.parametrize("username, password, role, email, expected_status", [
    # ("test_123123", "123123", "developer", "17637216311@163.com", 200)
    ("test_update", "123123", "developer", "13637216311@163.com", 200)
])
def test_create_user(username, password, role, email, expected_status):
    payload = {
        "username": username,
        "password": password,
        "role": role,
        "email": email
    }

    result = requests.post(USER_MANAGE, json=payload)

    print(result.status_code)
    print(result.json())

    assert result.status_code == expected_status


@pytest.mark.parametrize("page, page_size, expected_status", [
    (1, 10, 200)
])
def test_get_user_list(page, page_size, expected_status):
    result = requests.get(USER_MANAGE, params={"page": page, "page_size": page_size})
    print(result.status_code)
    print(result.json())

    assert result.status_code == 200


@pytest.mark.parametrize("id, expected_status", [
    (6, 200)
])
def test_delete_user_by_id(id, expected_status):
    result = requests.delete(f"{USER_MANAGE}/{id}")
    print(result.status_code)
    print(result.json())

    assert result.status_code == 200


@pytest.mark.parametrize("id, email, role, expected_status", [
    (7, "16337216311@163.com", "developer", 200)
])
def test_update_user(id, email, role, token, expected_status):
    payload = {     # 这里不要 id，因为 id 是路径参数
        "email": email,
        "role": role
    }
    # id=7 的 token
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0X3VwZGF0ZSIsInVzZXJfaWQiOjcsInJvbGUiOiJkZXZlbG9wZXIiLCJleHAiOjE4Mzc3NTM3NTV9.DESHUegJkuXY0J0lx4s9IKYhf2RzvIW2oSyQjvIh3aA"
    result = requests.put(f"{USER_MANAGE}/{id}", json=payload, headers={"Authorization": f"Bearer {token}"})
    print(result.status_code)
    print(result.json())

    assert result.status_code == expected_status


@pytest.mark.parametrize("id, expected_status", [
    (3, 200)
])
def test_get_user_detail(id, token, expected_status):
    result = requests.get(f"{USER_MANAGE}/{id}", headers={"Authorization": f"Bearer {token}"})
    print(result.status_code)
    print(result.json())

    assert result.status_code == expected_status


@pytest.mark.parametrize("id, old_password, new_password, expected_status", [
    (7, "123123", "112233", 200)
])
def test_change_password(id, old_password, new_password, token, expected_status):
    payload = {
        "old_password": old_password,
        "new_password": new_password
    }
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0X3VwZGF0ZSIsInVzZXJfaWQiOjcsInJvbGUiOiJkZXZlbG9wZXIiLCJleHAiOjE4Mzc3NTM3NTV9.DESHUegJkuXY0J0lx4s9IKYhf2RzvIW2oSyQjvIh3aA"
    result = requests.put(f"{USER_MANAGE}/{id}/password", json=payload, headers={"Authorization": f"Bearer {token}"})
    print(result.status_code)
    print(result.json())

    assert result.status_code == expected_status


@pytest.mark.parametrize("email, expected_status", [
    ("16337216311@163.com", 200)
])
def test_forget_password(email, expected_status):   # 这里不能频繁的运行，因为这里有频率限制
    payload = {
        "email": email
    }
    result = requests.post(SEND_CODE, params=payload)   # 这里不用 json；因为后端接口中的 email：str，是普通的参数，不是 Pydantic 类型
    print(result.status_code)
    print(result.json())

    assert result.status_code == expected_status


# @pytest.mark.parametrize("email, code, expected_status", [
#     ("16337216311@163.com", "以实际的 code 为准", 200)
# ])
# def test_verify_code(email, code, expected_status):
#     payload = {
#         "email": email,
#         "code": code
#     }
#     result = requests.post(VERIFY_CODE, params=payload)
#     print(result.status_code)
#     print(result.json())
#
#     assert result.status_code == expected_status



# @pytest.mark.parametrize("email, code, new_password, expected_status", [
#     ("16337216311@163.com", "以实际的 code 为准", "12344321", 200)
# ])
# def test_reset_password(email, code, new_password, expected_status):
#     payload = {
#         "email": email,
#         "code": code,
#         "new_password": new_password
#     }
#     result = requests.post(RESET_PASSWORD, params=payload)
#     print(result.status_code)
#     print(result.json())
#
#     assert result.status_code == expected_status


@pytest.mark.parametrize("name, description, expected_status", [
    ("test_April_twenty_seven", "4.27 接口自动化测试用例", 200)
])
def test_create_project(name, description, token, expected_status):
    payload = {
        "name": name,
        "description": description
    }
    result = requests.post(PROJECTS_MANAGE, json=payload, headers={"Authorization": f"Bearer {token}"})
    print(result.status_code)
    print(result.json())

    assert result.status_code == expected_status



@pytest.mark.parametrize("page, page_size, expected_status", [
    (1, 10, 200)
])
def test_get_project_list(page, page_size, token, expected_status):
    result = requests.get(PROJECTS_MANAGE, params={"page": page, "page_size": page_size}, headers={"Authorization": f"Bearer {token}"})
    print(result.status_code)
    print(result.json())

    assert result.status_code == expected_status