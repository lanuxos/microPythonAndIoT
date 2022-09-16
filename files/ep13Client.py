# EP.13 get temperature and humidity from DHT22 sensor which attaches on ESP-32 running mini server
import socket
import threading
import time
import csv
from datetime import datetime

def writeCSV(data):
    with open('ep13TempLog.csv', 'a', newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)

serverIp = '192.168.43.62'
port = 80

def getTemp():
    while True:
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.connect((serverIp, port))
        server.send('PC|TEMP'.encode('utf-8'))
        data = server.recv(1024).decode('utf-8')
        server.close()
        print(data)
        stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        t, h = data.split('_')
        dt = [stamp, t,h]
        writeCSV(dt)
        time.sleep(10)

getTemp()