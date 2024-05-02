@echo off

rem 激活虚拟环境
call .\myenv\Scripts\activate

rem 进入项目目录
cd .\backend\

rem 运行 Django 服务器
python manage.py runserver
