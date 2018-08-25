# -*- conding:utf-8 -*-

from django.db import models

# Create your models here.
class UserMessage(models.Model):
    object_id=models.CharField(max_length=20,primary_key=True,verbose_name=u'主键',default='')
    name=models.CharField(max_length=20,verbose_name='用户名')
    email=models.EmailField(verbose_name='邮箱')
    addresss=models.CharField(max_length=100,verbose_name=u'联系地址')
    message=models.CharField(max_length=500,verbose_name=u'留言信息',default='')

    class Meta:
        verbose_name=u'用户留言信息'
        verbose_name_plural=verbose_name
