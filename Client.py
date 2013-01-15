import socket
import sys

HOST, PORT = "localhost", 597
data = raw_input("Enter a message to send to server: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((HOST, PORT))
    sock.sendall(data + "\n")
    received = sock.recv(1024)
finally:
    sock.close()

print "Server: {}".format(received)