#!/usr/bin/env python3
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
# \r\n: is return a new line
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data)< 1:
        break
    print(data.decode(), end="")


mysock.close()