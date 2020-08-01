'''# from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers

# Create your views here.
class AccountInfoView(ModelViewSet):
    # queryset是一个查询数据的查询集，存储这所有的数据库查询之后的数据
    queryset = models.Account.objects.all()
    # serializer_class用来指定在当前的视图里面进行　序列化与反序列时使用的序列化器（串行器）
    serializer_class = serializers.AccountInfoSerializer'''

# coding:utf-8
import json
import datetime
import hashlib

from django.http import HttpResponse
from rest_framework.views import APIView
from . import models


# UsrLogin 
class UsrLogin(APIView):

# 定义请求方法为post，这种方法需要继承rest_framework的APIView
    def post(self, request):
        # 取到request对象的body（json）
        parameter_json = request.body
        # json转字典
        parameter = json.loads(parameter_json)

        #定义请求里的key
        get_accountname = 'accoutname'
        get_password = 'password'
        data = {
            'status': 'false',
            'message': 'error!',
            'data': 'null'
        }

        def get_json_Response(datas):
            return json.dumps(datas)
        #这个是初始化一个公共类，后面无效参数都调用这里的一个无效参数的字典，然后再转json，返回给客户端
        get_Response_public = get_json_Response(data)
        # 如果定义的get_phone和get_password都在请求的json中忘下走
        if get_accountname in parameter and get_password in parameter:
            #取出其request.json中的phone和password
            accountname = parameter[get_accountname]
            password = parameter[get_password]
            print(accountname,password)
            # 如果phone和password都不为空
            if accountname and password:
                #通过在model创建用户表通过取出的手机号和密码模糊查询是否有这个手机号和对应的密码
                inspect_account = models.Account.objects.filter(account_name=accountname, password=password)
                print(inspect_account)
                #判断inspect_phone是否为空
                if  inspect_account:
                    inspect = True
                else:
                    inspect = False
                #如果用户表有这个手机号，走正常登录逻辑
                if inspect == True:
                    #写一个方法通过sha256加密生成token
                    def _token_value(value):
                        token_hash = hashlib.sha256()
                        token_hash.update(value.encode('utf-8'))
                        return (token_hash.hexdigest())
                    #获取现在的时间转str
                    nowtime_to_token = datetime.datetime.today()
                    nowtime_to_token = str(nowtime_to_token)
                    #定义原字符串是目前时间加上手机号和密码
                    get_user_str = str(accountname+password+nowtime_to_token)
                    #通过上面sha256加密原字符串
                    get_token = _token_value(get_user_str)
                    # 根据请求的手机号密码查询出用户
                    inster_token = models.Account.objects.filter(account_name=accountname, password=password)
                    # 取出对象（查询到的用户数据），这个for可以不用因为唯一性的数据，直接索引，懒得改了
                    value = inster_token[0]
                    value.token_value = get_token
                    #把上面的加密的token保存到这个用户数据库token_value字段中
                    value.save()

                    #取出对象（查询到的用户数据），这个for可以不用因为唯一性的数据，直接索引，懒得改了，其实上面已经取过了，懒得改
                    #想把用户名取出来返回出去
                    name_info = [value.account_name, value.token_value]

                   # 返回字典
                    datas = {
                        'status': 'true',
                        'message': '登录成功！',
                        'name':name_info[0],
                        'token':get_token
 
                    }
                    # 字典转json返回给客户端
                    return HttpResponse(get_json_Response(datas),
                                        content_type="application/json,charset=utf-8")
               # 异常情况
                else:
                    datas = {
                        'status': 'false',
                        'message': '手机号或密码不正确！',
                        'data': 'null'
 
                    }
 
                    return HttpResponse(get_json_Response(datas),
                                        content_type="application/json,charset=utf-8")
 
            # 异常情况 公共方法
            else:
                return HttpResponse(get_Response_public.InvalidParameter(),
                                    content_type="application/json,charset=utf-8")
                # 异常情况 公共方法
        else:
            return HttpResponse(get_Response_public.InvalidParameter(), content_type="application/json,charset=utf-8")