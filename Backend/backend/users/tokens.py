# tokens.py
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class CustomRefreshToken(RefreshToken):
    @classmethod
    def for_user(cls, user):
        token = cls()
        token['user_id'] = str(user.id)  # 使用你的自定义用户模型的主键字段
        token['username'] = user.get_username()
        return token
