# MicroPython and IoT
# ep.6 - Standalone code

# EP introduction
# boot.py && main.py - 003300
# Standalone blinking LED - 004200
    ```
        from machine import Pin
        import time
        led = Pin(23, Pin.OUT)
        for i in range(60):
            led.on()
            time.sleep(1)
            led.off()
            time.sleep(1)
    ```
# Server
```
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
    client.send('receved you messages.'.encode('utf-8'))
    client.close()

```
# Client - 013730
```
import socket
import network
import time
# from machine import Pin
# serverIP = '178.128.125.82'
serverIP = '192.168.43.12'
port = 9000
buffSize = 4096

def send_data(data):
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.connect((serverIP, port))
    server.send(data.encode('utf-8'))
    data_server = server.recv(1024).decode('utf-8')
    print('Server: ', data_server)
    server.close()
    
wifi = 'LaHotspot'
password = 'Nilavath'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
time.sleep(2)
wlan.connect(wifi, password)
time.sleep(2)
print(wlan.isconnected())
send_data('microPythonESP-12f')
```
# GUI - 020500
```
from tkinter import *
import socket
import threading

def runserver():
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
        # dataConstructure = 'LED:ON'
        data_split = data.split(':')
        if data_split[1] == 'ON':
            status.set(f'Status from ESP-12f is {data_split[1]}')
            l2.configure(fg='green')
        else:
            status.set(f'Status from ESP-12f is OFF')    
            l2.configure(fg='red')
        client.send(f'Server have received you messages: [{data}].'.encode('utf-8'))
        client.close()

gui = Tk()
gui.geometry('500x300')
gui.title('MicroPython GUI Dashboard')
l1 = Label(gui, text='ESP-12f Status')
l1.pack()
status = StringVar()
status.set('### ESP-12f Status Show Here ###')
l2 = Label(gui, textvariable=status)
l2.configure(fg='green')
l2.pack()

# threading - for parallel running
task = threading.Thread(target=runserver)
task.start()

gui.mainloop()
```