import socket
import sys

HOST, PORT = "localhost", 9087 #Set DMServer

print('DMNet Console v0.1')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Create socket connection to DMServer
while True:
	data = input("->")
	print(data)
	sock.sendto(bytes(data, "utf-32"), (HOST, PORT)) #Send dat, NOTE! DMServer support only UTF-32 encoding!
	received = str(sock.recv(4098), "utf-32") #Recieve response from DMServer
	print('[ Server ] :: '+received)
