import socket

HOST = '10.3.43.192'
PORT = 9099

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
socket.connect((HOST,PORT))

socket.send("Hello World!".encode('utf-8'))