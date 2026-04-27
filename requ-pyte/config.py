BASE_URL = "http://127.0.0.1:8000"

# 接口路由
"""
用户认证
"""
LOGIN_URL = f"{BASE_URL}/auth/login"
USER_INFO = f"{BASE_URL}/auth/me"
""""
用户管理
"""
USER_MANAGE = f"{BASE_URL}/users"
"""
忘记密码
"""
SEND_CODE= f"{BASE_URL}/password-reset/send-code"
VERIFY_CODE = f"{BASE_URL}/password-reset/verify-code"
RESET_PASSWORD = f"{BASE_URL}/password-reset/reset-password"
"""
项目管理
"""
PROJECTS_MANAGE = f"{BASE_URL}/projects"