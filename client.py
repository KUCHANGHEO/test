import socket
com_socket= socket.socket()
com_socket.connect(('192.168.24.102',20000))

while True:
    send_data = input("message:")
    com_socket.send(bytes(send_data,"UTF-8"))
    print(com_socket.recv(4096).decode("UTF-8"))
