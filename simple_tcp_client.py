import socket
host = "www.google.com"
port = 80

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client to the server
client.connect((host,port))

# Send data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Receive data
print client.recv(4096)
