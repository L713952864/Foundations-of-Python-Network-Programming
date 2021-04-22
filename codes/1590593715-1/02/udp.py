#!/usr/bin/env python
# UDP Example - Chapter 2

import socket, sys, time
# UDP客户端， python udp.py localhost 51423

host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    port = int(textport)
except ValueError:
    # That didn't work.  Look it up instread.
    port = socket.getservbyname(textport, 'udp')

s.connect((host, port))  # 可以不使用connect() 看udptime.py
print("Enter data to transmit: ")
data = sys.stdin.readline().strip()
s.sendall(data.encode())
s.shutdown(1)
print("Looking for replies; press Ctrl-C or Ctrl-Break to stop.")
while 1:
    # 服务器也许不会返回任何数据，或者数据在传输过程中丢失，程序判断不出来
    buf = s.recv(2048)
    if not len(buf):
        break
    print("Received: %s" % buf.decode())
