#!/usr/bin/env python
# Simple Gopher Client - Chapter 1 - gopherclient.py
# 外部打开终端，输入命令行: python xxx.py quux.org /
import socket, sys

port = 70 # Gopher协议，从主机上请求相关文档
host = sys.argv[1]   # sys.argv[]从程序外部获取参数
filename = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 注意端口
# 也可以直接写 s = socket.socket() 默认参数 (鼠标指向不动，会出现形参)
# 其中参数family: socket.AF_INET 用于服务器与服务器之间的网络通信， socket.AF_INET6
# 另一个参数type套接字类型: socket.SOCK_STREAM 用于TCP流式通信，socket.SOCK_DGRAM 用于UDP数据报式通信

s.connect((host, port))

s.sendall(filename + "\r\n")

while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    f = open('gopherclient.txt' ,'w')
    f.write(buf)
    # sys.stdout.write(buf)
    
