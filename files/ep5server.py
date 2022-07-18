import socket

serverip = '192.168.43.12'
port = 9000
buffersize = 4096
while True:
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((serverip, port))
    server.listen(1)
    print('waiting for connect...\n')
    client, addr = server.accept()
    print('Connected from: \n', addr)
    data = client.recv(buffersize).decode('utf-8')
    print('Data from client: \n', data)
    client.send('received you messages.'.encode('utf-8'))
    client.close()
