#!/usr/bin/env python3

import socket  # Importing the socket library to enable network communication

# Create a socket object for network communication.
# AF_INET specifies the address family (IPv4).
# SOCK_STREAM specifies the socket type (TCP - a reliable, connection-based protocol).
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to a remote server at 'data.pr4e.org' on port 80 (HTTP port).
mysock.connect(('data.pr4e.org', 80))

# Prepare the HTTP GET request command to fetch the specified page.
# The '\r\n\r\n' marks the end of the request headers.
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()  
# Encoding the string to bytes, as the socket requires byte data to send.

# Send the HTTP GET request to the server.
mysock.send(cmd)

# Enter a loop to receive data from the server in chunks.
while True:
    # Receive up to 512 bytes of data from the server.
    data = mysock.recv(512)
    # If no data is received (connection closed by the server), break the loop.
    if len(data) < 1:
        break
    # Decode the received bytes back into a string and print to the console.
    # 'end=""' avoids adding extra newlines after each print.
    print(data.decode(), end="")

# Close the socket connection after data is fully received and processed.
mysock.close()
