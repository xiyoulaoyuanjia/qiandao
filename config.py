#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Author: Binux<i@binux.me>
#         http://binux.me
# Created on 2014-07-30 12:21:48

import hashlib

debug = True
gzip = True
bind = '0.0.0.0'
port = 8923
https = False
cookie_days = 5

class mysql(object):
    host = 'localhost'
    port = '3306'
    database = 'qiandao'
    user = 'qiandao'
    passwd = None

class redis(object):
    host = 'localhost'
    port = 6379
    passwd = None
    db = 1
evil = 100

pbkdf2_iterations = 400
aes_key = hashlib.sha256('binux').digest()
cookie_secret = hashlib.sha256('binux').digest()
check_task_loop = 10000
download_size_limit = 1*1024*1024
proxies = []

mailgun_key = ""
ga_key = ""

try:
    from local_config import *
except ImportError:
    pass
