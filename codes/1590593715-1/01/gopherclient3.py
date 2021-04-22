#!/usr/bin/env python
# Simple Gopher Client with file-like interface - Chapter 1
# gopherclient3.py

import socket, sys

port = 70
host = sys.argv[1]
filename = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
# 接收返回的数据，返回一个与套接字相关的文件对象，像操作一个文件一样去操作一个socket连接
# fd = s.makefile('rw', 0) # 书上例子
fd = s.makefile('rw', buffering=1)

fd.write(filename + "\r\n")  # = s.send()

for line in fd.readlines():
    sys.stdout.write(line)
    
