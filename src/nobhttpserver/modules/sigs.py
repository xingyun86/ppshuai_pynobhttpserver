#!coding:utf-8
#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-

import sys
import signal
from utils import CUtils

'''
定义CTRL+C退出信号处理
'''
def signal_exit_action(signum, params):
    CUtils.python_printf("===============[[[User press ctrl+c close program]]]===============")
    sys.exit(0)
    
class CSigs:
    def __init__(self):
        pass
    # 注册CTRL+C的信号处理
    @staticmethod
    def reg_sig(action=signal_exit_action):
        # 注册CTRL+C的信号处理
        signal.signal(signal.SIGINT, action)
        signal.signal(signal.SIGTERM, action)
