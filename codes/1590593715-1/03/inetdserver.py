#!/usr/bin/env python
# Basic inetd server - Chapter 3 - inetdserver.py
'''
xinetd 或者 inetd 是Unix系统上的程序，在linux中运行
绑定监听接收多个服务器端口，有响应的客户端来请求，就调用相应的服务端程序传socket
避免服务器一直运行却没有客户端来连的空闲进程，从而浪费内存
通过xinetd or inetd来为连接分配一个进程，每当一个客户端连接，一个新的服务器就启动
但是UDP无连接，该怎么办
'''

import sys
print("Welcome.")
print("Please enter a string:")
sys.stdout.flush()  # 一般sys.stdout是被缓冲的，调用flush()确保输出被立即传输
line = sys.stdin.readline().strip()
print("You entered %d characters." % len(line))
