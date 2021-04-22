#!/usr/bin/env python
# Get list of available socket options -- Chapter 3 -- sockopts.py
# 给出支持的socket选项
import socket
solist = [x for x in dir(socket) if x.startswith('SO_')]
solist.sort()
for x in solist:
    print(x)

