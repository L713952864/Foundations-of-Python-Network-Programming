#!/usr/bin/env python
# UDP Connectionless Example - Chapter 2 - udptime.py

import socket, sys, struct, time

hostname = 'time.nist.gov'
port = 37

#host = socket.gethostbyname(hostname)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = 'hello'
s.sendto(msg.encode(), ('localhost', 51423))

print("Looking for replies; press Ctrl-C to stop.")
# 不能保证这个信息包能够被成功传送，还有些防火墙会阻止UDP通信
buf = s.recvfrom(2048)[0]  # 调用recvfrom()返回一个tuple(实际接收数据, 发送数据的机器地址)
if len(buf) != 4:
    print("Wrong-sized reply %d: %s" % (len(buf), buf))
    sys.exit(1)

secs = struct.unpack("!I", buf)[0]
secs -= 2208988800  # 减去1900年到1970年的秒数，转换成UNIX的时间格式
print(time.ctime(int(secs)))

