#!/usr/bin/env python
# Socket-based inetd server - Chapter 3 - inetdsocket.py

import sys, socket, time
# fromfd()需要一个文件数量和一些标准参数
s = socket.fromfd(sys.stdin.fileno(), socket.AF_INET, socket.SOCK_STREAM)
s.sendall("Welcome.\n")
s.sendall("According to our records, you are connected from %s.\n" % \
          str(s.getpeername()))
s.sendall("The local time is %s.\n" % time.asctime())
