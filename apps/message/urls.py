#!/usr/bin/python3
#coding:utf-8

"""
@author: Seven°
@contact: free001@vip.qq.com
@software: PyCharm
@file: urls.py
@time: 2018-08-25 11:15
"""
from django.conf.urls import url
from message.views import *

urlpatterns =[
    url(r'^form',getform_views),
]