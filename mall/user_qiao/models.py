#encoding=utf-8
from django.db import models
#encoding=utf-8
from django.db import models
from goods_qi.models import GoodsInfo

from cart_kun.models import  *


class UserInfo(models.Model):
    id = models.AutoField
    uname=models.CharField(max_length=40)#用户名
    upwd=models.CharField(max_length=50)#密码
    isDelete=models.BooleanField(default=False)#逻辑删除
    recipients=models.CharField(max_length=40)#收件人
    address=models.CharField(max_length=60)#收货地址
    phone=models.CharField(max_length=20)#联系电话




