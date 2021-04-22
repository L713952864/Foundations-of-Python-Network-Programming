#!/usr/bin/env python
# Simple Server - Chapter 1 - server.py
import socket

host = ''      # 服务器可以来自任何地方的连接       # Bind to all interfaces
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 通常一个服务器进程终止后，操作系统会保留几分钟它的端口，防止其他进程甚至自己的一个实例在这几分钟内使用这个端口
# 设置SO_REUSEADDR为true则会立马释放该端口
s.bind((host, port))
s.listen(1)  # 每次最多只有一个等待处理的连接，真实情况数字很大

print("Server is running on port %d; press Ctrl-C to terminate." \
      % port)
# print("Server is running on port " + str(port))

while 1:
    clientsock, clientaddr = s.accept()  # server接收到了来自客户端的信息
    # 实际上在等待客户端连接的时候，程序阻塞，不使用任何CPU资源
    clientfile = clientsock.makefile('rw', buffering=1)  # 如果设为0关掉缓冲，报错unbuffered streams must be binary
    str1 = "Welcome, " + str(clientaddr) + "\n"
    clientfile.write(str1)
    str2 = "Please enter a string:"
    clientfile.write(str2)

    line = clientfile.readline().strip()
    clientfile.write("You entered "+str(len(line))+" characters.\n")
    clientfile.close()
    clientsock.close()

