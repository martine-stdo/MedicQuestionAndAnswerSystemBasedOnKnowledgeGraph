# views.py
from rest_framework.decorators import api_view,authentication_classes
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import UserSerializer
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model
from .tokens import CustomRefreshToken
import openai



# 注册
@api_view(['POST'])
def register_user(request):
    # 从请求数据中获取用户名和密码
    username = request.data.get('userAccount')
    password = request.data.get('userPassword')
    
    # 检查用户名和密码是否存在
    if not username or not password:
        return Response({'error': 'Both username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # 检查用户名是否已经存在
    if CustomUser.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # 检查密码是否为空
    if not password:
        return Response({'error': 'Password cannot be empty.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # 创建用户并序列化用户数据
    user = CustomUser.objects.create_user(username=username, password=password)
    serializer = UserSerializer(user)
    
    # 返回成功响应
    return Response({'code': 200, 'message': 'Registration successful', 'user': serializer.data}, status=status.HTTP_201_CREATED)

# 登陆
@api_view(['POST'])
def login_user(request):
    # 从请求数据中获取用户名和密码
    username = request.data.get('userAccount')
    password = request.data.get('userPassword')
    
    print(f"username:{username} password:{password}")
    
    # 使用自定义的身份验证后端进行身份验证
    user = authenticate(request, username=username, password=password)
    print(user)
    
    # 如果用户不存在，返回错误响应
    if user is None:
        return Response({'message': '用户不存在或者密码错误'})
    
# 生成新的访问令牌和刷新令牌
    refresh = CustomRefreshToken.for_user(user)
    token = str(refresh.access_token)
    
    # 序列化用户数据
    serializer = UserSerializer(user)
    
    # 返回成功响应，包含访问令牌和用户数据
    return Response({'code': 0, 'token': token, 'user': serializer.data}, status=status.HTTP_200_OK)


# chatbot
openai.api_key = 'sk-proj-J0mfgcyhoprfs6uYwYC5T3BlbkFJFtgfULeNTLxGR2upIx3R'
@api_view(['POST'])
def chat_view(request):
    if request.method == 'POST':
        # 检查请求数据中是否存在 'question' 字段且不为空
        if 'question' not in request.data or not request.data['question']:
            return JsonResponse({'message': '请在请求中提供非空的问题字段'}, status=400)

        try:
            # 从请求数据中提取用户的问题
            user_question = request.data['question']

            # 构建 OpenAI API 请求并发送，获取模型的响应
            response = openai.Completion.create(
                engine="gpt-3.5-turbo",  # 选择模型
                prompt="假如你是一个医学助理，你只回答医学相关的问题：" + user_question,  # 将用户的问题作为提示
                max_tokens=50  # 设置生成的最大标记数
            )

            # 解析并将模型的响应返回给前端
            bot_reply = response.choices[0].text.strip()
            return JsonResponse({'reply': bot_reply})

        except openai.error.OpenAIError as e:
            # 处理 OpenAI API 的错误
            return JsonResponse({'message': str(e)}, status=500)

    else:
        # 处理除 POST 方法外的其他请求
        return JsonResponse({'message': '只允许使用 POST 方法'}, status=405)