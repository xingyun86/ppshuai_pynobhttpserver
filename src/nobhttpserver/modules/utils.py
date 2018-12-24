#!coding:utf-8
#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-

import os
import sys
import time
import json

class CUtils:
    def __init__(self):
        pass
    '''
    定义专用打印日志参数
    '''
    @staticmethod
    def python_printf(x):
        print "["+time.strftime('%Y-%m-%d %H:%M:%S',
                                 time.localtime(int(round(time.time()*1000))/1000))+"]\x20"+x

    '''
    定义获取日期函数方法
    '''
    @staticmethod
    def current_day():
        return time.mktime(time.strptime(time.strftime('%Y-%m-%d', time.localtime(int(round(time.time()*1000))/1000)), "%Y-%m-%d"))

    '''
    获取脚本自身路径
    '''
    @staticmethod
    def self_path():
        path = os.path.realpath(sys.argv[0])
        if os.path.isfile(path):
            path = os.path.dirname(path)
        return os.path.abspath(path)

    '''
    读取JSON配置文件参数
    '''
    @staticmethod
    def read_json(fname):
        f = open(fname, "rb")
        t = f.read()
        f.close()
        return json.loads(t)
    
    '''
    读取JSON配置文件参数
    '''
    @staticmethod
    def read_json_ex(fname, encoding="utf-8"):
        f = open(fname, "rb")
        t = f.read()
        f.close()
        return json.loads(t.encode(encoding=encoding), encoding=encoding)

    '''
    创建文件夹
    '''
    @staticmethod
    def py_mkdir(path):
    
        folder = os.path.exists(path)
    
        if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
        return os.path.exists(path)

    '''
    删除文件
    '''
    @staticmethod
    def py_unlink(path):
        try:
            os.system("rm -rf "+path)
            os.remove(path)
            os.unlink(path)
        except Exception, e:
            pass