# from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers

# Create your views here.
class AccountInfoView(ModelViewSet):
    # queryset是一个查询数据的查询集，存储这所有的数据库查询之后的数据
    queryset = models.Account.objects.all()
    
    # serializer_class用来指定在当前的视图里面进行　序列化与反序列时使用的序列化器（串行器）
    serializer_class = serializers.AccountInfoSerializer