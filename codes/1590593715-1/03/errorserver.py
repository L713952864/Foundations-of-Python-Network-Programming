#!/usr/bin/env python
# Server With Error Handling - Chapter 3 - errorserver.py
import socket, traceback

host = ''                               # Bind to all interfaces
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

while 1:
    try:
        clientsock, clientaddr = s.accept()
    except KeyboardInterrupt:  # 像之前一样CTRL+C就会终止服务器程序
        raise
    except:  # 其他所有的异常被打印出来
        traceback.print_exc()
        continue  # 程序不会终止

    # Process the connection

    try:
        print("Got connection from" + clientsock.getpeername())
        # Process the request here
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()

    # Close the connection

    try:
        clientsock.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
