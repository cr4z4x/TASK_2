import socket



HOST='10.3.43.192'
PORT=9090
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
server.bind((HOST,PORT))

server.listen()


while True:
    com_sock,address = server.accept()
    print(f"connected to {address}")
    message = com_sock.recv(1024).decode('utf-8')
    print(f"Message{message}")
    com_sock.close()