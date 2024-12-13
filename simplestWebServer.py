#!/usr/bin/env python3

from socket import *

def createServer():
    # it's like creating a phone :
    serversocket = socket(AF_INET, SOCK_STREAM)

    try:
        # receive the phone calls on port 9000
        serversocket.bind(('localhost',9000))
        # it says dear OS, if I am handling a phone call you can hold on 4 more and queue them
        serversocket.listen(5)

        while(1):
            (clientsocket, address) = serversocket.accept()
            rd = clientsocket.recv(5000).decode() # decode it to utf-8
            pieces = rd.split("\n")
            if (len(pieces) > 0 ): print(pieces[0])

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"

            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)


    except KeyboardInterrupt:
        print("/nShutting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)
    serversocket.close()

print('Access http://localhost:9000')
createServer()
