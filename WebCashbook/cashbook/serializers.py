'''
序列化模块
'''
from rest_framework import serializers
from . import models

class AccountInfoSerializer(serializers.ModelSerializer):
    '''
    AccountInfoSerializer 账户信息序列化类
    '''
    class Meta:
        fields = ('id', 'account_name', 'account_password', 'created_at', 'updated_at',)
        model = models.Account
