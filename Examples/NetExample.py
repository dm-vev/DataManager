import socket
import sys

HOST, PORT = "localhost", 9087

print('DMNet Console v0.1')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
	data = input("->")
	print(data)
	sock.sendto(bytes(data, "utf-32"), (HOST, PORT))
	received = str(sock.recv(4098), "utf-32")
	print('[ Server ] :: '+received)
