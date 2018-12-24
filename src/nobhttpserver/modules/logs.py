#!coding:utf-8
#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-

import time
import logging
import logging.handlers


class CLogs:
    logger = None
    fhandler = None
    shandler = None

    def __init__(self, name, file_name, max_bytes=10*1024*1024, backup_count=10):
        # logging初始化工作
        logging.basicConfig()
        # 写入文件，如果文件超过max_bytes个Bytes，仅保留backup_count个文件。
        self.fhandler = logging.handlers.RotatingFileHandler(
            file_name, maxBytes=max_bytes, backupCount=backup_count)
        self.fhandler.setLevel(logging.INFO)
        # self.fhandler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))
        self.fhandler.setFormatter(logging.Formatter(
            fmt="[%(asctime)s.%(msecs)03d],%(message)s", datefmt='%Y-%m-%d %H:%M:%S'))

        # 在控制台打印日志
        self.shandler = logging.StreamHandler()
        self.shandler.setLevel(logging.DEBUG)
        self.shandler.setFormatter(logging.Formatter(
            fmt="[%(asctime)s.%(msecs)03d] - %(levelname)s - %(message)s", datefmt='%Y-%m-%d %H:%M:%S'))

        # myapp的初始化工作
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(self.shandler)
        self.logger.addHandler(self.fhandler)

    '''
    关闭日志句柄
    '''

    def logger_shutdown(self):
        self.logger.removeHandler(self.shandler)
        self.logger.removeHandler(self.fhandler)
        logging.shutdown()
