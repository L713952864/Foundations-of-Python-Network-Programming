#!/usr/bin/env python
# Information Example - Chapter 2

import socket

print("Creating socket...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("done.")

print("Looking up port number...")
port = socket.getservbyname('http', 'tcp')
print("done.")

print("Connecting to remote host on port %d..." % port,)
s.connect(("www.google.com", port))
print("done.")

print("Connected from", s.getsockname())  # 显示本身的
print("Connected to", s.getpeername())  # 显示远程机器的IP地址和端口
