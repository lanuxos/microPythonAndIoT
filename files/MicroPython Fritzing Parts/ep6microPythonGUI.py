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
