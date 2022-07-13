# MicroPython and IoT
# ep.7 - DHT22 temperature/humidity sensor

# EP introduction
# Sensor specification
# Concept - 003900
# DHT22 - 010000
```
from machine import Pin
import dht
d = dht.DHT22(Pin(23))
d.measure()
print(d.temperature())
print(d.humidity())
```
# DHT22 value to server - 015130
```
import socket
import network
import time
from machine import Pin
# serverIP = '178.128.125.82'
serverIP = '192.168.43.12'
port = 9000
buffSize = 4096

import dht
d = dht.DHT22(Pin(23))
d.measure()
print(d.temperature())
print(d.humidity())

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

for i in range(10):
    d.measure()
    time.sleep(1)
    temp = d.temperature()
    humid = d.humidity()
    text = f'Temp:{temp}'
    send_data('temp:21')
    time.sleep(3)
    print('-=0=-')
```
# GUI - 021700
```
from tkinter import *
import socket
import threading

def runserver():
    serverip = '192.168.43.12'
    port = 9001
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
        if float(data_split[1]) > 26:
            print('hot: ', data_split[1])
            img = PhotoImage(file='level3.png')
            ICON.configure(image=img)
            ICON.image = img
            status.set(f'Temperature is hot / {data_split[1]}')
            l2.configure(fg='red')
        elif float(data_split[1]) > 25.5:
            print('warm: ', data_split[1])
            img = PhotoImage(file='level2.png')
            ICON.configure(image=img)
            ICON.image = img
            status.set(f'Temperature is warm / {data_split[1]}')
            l2.configure(fg='yellow')
        else:
            print('cool: ', data_split[1])
            img = PhotoImage(file='level1.png')
            ICON.configure(image=img)
            ICON.image = img
            status.set(f'Temperature is cool / {data_split[1]}')
            l2.configure(fg='green')
        '''
        if data_split[1] == 'ON':
            status.set(f'Status from ESP-12f is {data_split[1]}')
            l2.configure(fg='green')
        else:
            status.set(f'Status from ESP-12f is OFF')    
            l2.configure(fg='red')
        '''
        client.send(f'Server have received you messages: [{data}].'.encode('utf-8'))
        client.close()

gui = Tk()
gui.geometry('500x500')
gui.title('MicroPython GUI Dashboard')
l1 = Label(gui, text='ESP-12f Status')
l1.pack()
status = StringVar()
status.set('### ESP-12f Status Show Here ###')
l2 = Label(gui, textvariable=status)
l2.configure(fg='green')
l2.pack()

img = PhotoImage(file='level1.png')
ICON = Label(gui, image=img)
ICON.pack()

# threading - for parallel running
task = threading.Thread(target=runserver)
task.start()

gui.mainloop()
```