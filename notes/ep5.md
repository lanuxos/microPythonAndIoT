# MicroPython and IoT
# ep.5 - Connect to internet [urequests]

# Review last EP.4 code
# Wi-fi concept - 002630
# [Manual](https://docs.micropython.org/en/latest/)
# Connect to wi-fi
```
import network
net = network.WLAN(network.STA_IF) # network.WLAN(network.AP_IF) for access point mode
net.active(True)
net.scan()
net.connect("SSID", "PASSWORD")
net.isconnected()
net.ifconfig()
```
# To convert mac address to hex
```
    import ubinascii
    print(uninascii.hexlify(net.config('mac'), ':').decode())
```
# Server - 021300
```
import socket

serverip = '192.168.0.100'
port = 9000
buffersize = 4096
while True:
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((serverip, port))
    server.listen(1)
    print('waiting for connect...')
    client, addr = server.accept()
    print('Connected from: ', addr)
    data = client.recv(buffersize).decode('utf-8')
    print('Data from client: ', data)
    client.send('receved you messages.'.encode('utf-8'))
    client.close()
    ```
# Client - 022200
```
import socket
serverip = '192.168.43.12'
port = 9000
def sendData(data):
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.connect((serverip, port))
    server.send(data.encode('utf-8'))
    data_server = server.recv(1024).decode('utf-8')
    print('Server: ', data_server)
    server.close()
```
# urequests - 025230
```
import urequests
result = urequests.get(url='http://uncle-machine.com/hello')
```