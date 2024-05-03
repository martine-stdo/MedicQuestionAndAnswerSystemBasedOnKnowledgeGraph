# Generated by Django 5.0.4 on 2024-05-01 14:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_customuser_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="password",
            field=models.CharField(max_length=128, verbose_name="password"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="user_role",
            field=models.CharField(
                choices=[("user", "用户"), ("admin", "管理员")],
                default="user",
                max_length=100,
            ),
        ),
    ]