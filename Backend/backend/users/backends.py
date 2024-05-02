from django.contrib.auth.backends import BaseBackend
from .models import CustomUser

class CustomUserAuthenticationBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            # 根据提供的用户名获取用户
            user = CustomUser.objects.get(username=username)
            # 验证用户密码
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            # 如果找不到用户，返回None
            return None

    def get_user(self, user_id):
        try:
            # 根据用户ID获取用户
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
