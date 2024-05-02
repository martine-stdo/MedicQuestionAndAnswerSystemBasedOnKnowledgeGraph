# models.py
import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, user_role='user', **extra_fields):
        # 检查是否提供了用户名
        if not username:
            raise ValueError('用户名必须设置')

        # 创建用户实例
        user = self.model(username=username, user_role=user_role, **extra_fields)
        
        # 设置密码并加密
        user.set_password(password)
        
        # 将用户保存到数据库
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        # 设置超级用户的默认值
        extra_fields.setdefault('user_role', 'admin')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # 检查是否将is_staff和is_superuser设置为True
        if extra_fields.get('is_staff') is not True:
            raise ValueError('超级用户必须具有is_staff=True。')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('超级用户必须具有is_superuser=True。')

        # 调用create_user方法创建超级用户
        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    # 用户唯一标识符
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # 用户名，必须唯一
    username = models.CharField(max_length=150, unique=True)

    # 密码字段
    password = models.CharField(max_length=128)

    # 用户头像URL，可选字段
    avatar_url = models.URLField(blank=True, null=True)

    # 用户角色，选择用户或管理员
    user_role = models.CharField(max_length=100, choices=[('user', '用户'), ('admin', '管理员')], default='user')

    # 用户是否激活
    is_active = models.BooleanField(default=True)

    # 用户是否是员工
    is_staff = models.BooleanField(default=False)

    # 用户是否是超级用户
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    # 将用户名字段指定为username
    USERNAME_FIELD = 'username'

    # 注册时不需要额外的必填字段
    REQUIRED_FIELDS = []

    def get_username(self):
        return getattr(self, self.USERNAME_FIELD)
