# MicroPython and IoT
# ep.9 - Relay

# EP introduction
# Relay - 003300
    - Active low mode - working when logic 0 apply
    - Active high mode - working when logic 1 apply
```
from machine import Pin
import time
# relay = Pin(23, Pin.OUT, Pin.PULL_UP)
relay = Pin(23, Pin.OUT)
relay.on() # power off
relay.off() # power on
relay.value(0) # power off
relay.value(1) # power on
def RelayOn():
    relay.value(0)
    print('LED: ON')
def RelayOff():
    relay.value(1)
    print('LED: OFF')
```
# LED - 021100
- RELAY/BOARD INTERFACE
    - DC+ <> 3.3V
    - DC- <> GND
    - IN1 <> GPIO
- RELAY/LED INTERFACE
    - COM1 <> GPIO
    - NO1 <> LED+
- LED INTERFACE
    - LED- <> GND
```
from machine import Pin
relay = Pin(23, Pin.OUT)
relay.value(1)
led = Pin(34, Pin.OUT)
led.on()
relay.value(0)
def On():
    relay.value(0)
    print('LED On')
def Off():
    relay.value(1)
    print('LED Off')
```