#!/usr/bin/env python
# High-Level Gopher Client with urllib - Chapter 1 - urlclient.py

import urllib.request, sys
# 命令行输入 python urlclient.py http://www.baidu.com
url = sys.argv[1]  # 注意输入url格式
# host = sys.argv[1]
# file = sys.argv[2]
'''
f = urllib.urlopen('gopher://%s%s' % (host, file))
for line in f.readlines():
    sys.stdout.write(line)
'''
f = urllib.request.urlopen(url)
for line in f.readlines():
    # 注意这里传输的是bytes
    sys.stdout.write(line.decode())
