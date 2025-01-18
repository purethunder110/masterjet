# Generated by Django 4.2 on 2024-11-23 16:23

import core.user.User
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_pluginmanager_alter_usermodel_jwt_auth_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='jwt_auth_token',
            field=models.CharField(default=core.user.User.UserModel.random_string, max_length=15),
        ),
    ]
