# ep.12
# socket, _thread
from machine import Pin, SoftI2C
import network
import time
import ssd1306
import socket
import _thread

led = Pin(23, Pin.OUT)
led.off()

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def wifi():
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        print('Connecting to wifi...')
        wlan.active(True)
        wlan.connect('LaHotspot', 'Nilavath')
        time.sleep(1)
        while not wlan.isconnected():
            pass
    ipAddr, _, _, _ = wlan.ifconfig()
    oled.fill(0)
    oled.text('Connected', 0, 0)
    oled.text(f'{ipAddr}', 0, 16)
    time.sleep(1)
    oled.show()
    print('Connected to:', ipAddr)
wifi()
html_on = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EP 12</title>
</head>
<body>
    <center>
    <img src="https://raw.githubusercontent.com/UncleEngineer/MicroPython-IoT/main/light-bulb-on.png" width="300">
    <form action="">
        <button type="submit" name="LED" value="ON">ON</button>
        <button type="submit" name="LED" value="OFF">OFF</button>
    </form>
    </center>
</body>
</html>
'''
html_off = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EP 12</title>
</head>
<body>
    <center>
    <img src="https://raw.githubusercontent.com/UncleEngineer/MicroPython-IoT/main/light-bulb-off.png" width="300">
    <form action="">
        <button type="submit" name="LED" value="ON">ON</button>
        <button type="submit" name="LED" value="OFF">OFF</button>
    </form>
    </center>
</body>
</html>
'''
global led_status
led_status = 'OFF'
def runserver():
    global led_status
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ''
    port = 80
    s.bind((host, port))
    s.listen(5)

    led_status = 'OFF'

    while True:
        client, addr = s.accept()
        print('Connected from: ', addr)
        data = client.recv(1024).decode('utf-8')
        print([data])
        '''check = data.split()[1].replace('/','').replace('?','')
        print('CHECK: ', check)
        client.send(html_on)
        client.close()
        '''
        try:
            check = data.split()[1].replace('/','').replace('?','')
            print('CHECK: ', check)
            if check != '':
                led_name, led_value = check.split('=')
                if led_value == 'ON':
                    print('Turn LED on')
                    led.on()
                    client.send(html_on)
                    client.close()
                    oled.fill(0)
                    oled.text('LED: ON', 0, 0)
                    oled.show()
                    led_status = 'ON'
                elif led_value == 'OFF':
                    print('Turn LED off')
                    led.off()
                    client.send(html_off)
                    client.close()
                    oled.fill(0)
                    oled.text('LED: OFF', 0, 0)
                    oled.show()
                    led_status = 'OFF'
            else:
                if led_status == 'OFF':
                    client.send(html_off)
                else:
                    client.send(html_on)
                
        except:
            pass

def loop_led():
    global led_status
    for i in range(100):
        led.on()
        led_status = 'ON'
        oled.fill(0)
        oled.text('LED: ON', 0, 0)
        oled.text('Loop 10s', 0, 8)
        oled.show()
        time.sleep(10)
        led.off()
        led_status = 'OFF'
        oled.fill(0)
        oled.text('LED: OFF', 0, 0)
        oled.text('Loop 10s', 0, 8)
        oled.show()
        time.sleep(10)

_thread.start_new_thread(runserver, ())
_thread.start_new_thread(loop_led, ())