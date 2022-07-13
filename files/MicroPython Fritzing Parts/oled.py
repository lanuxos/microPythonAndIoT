

# Display Image & text on I2C driven ssd1306 OLED display 128x64 px
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import machine
import utime

# sensor_temp = machine.ADC(4)
# conversion_factor = 3.3 / (65535)
# reading = sensor_temp.read_u16() * conversion_factor
# temperature = 27 - (reading - 0.706)/0.001721
# print(temperature)

def Position(text):
  if len(text) <= 16:
    text = text
    if len(text) == 16:
      result = 0
      return result
    else:
      start = (16 - len(text)) * 8
      mod = start % 2
      if mod == 0:
        result = start // 2
        return result
      else:
        result = (start // 2) + (mod / 2)
        return result
  else:
    text = text[:16]
    result = 0
    return result

WIDTH  = 128                                            # oled display width
HEIGHT = 64                                             # oled display height
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000)       # Init I2C using pins GP8 & GP9 (default I2C0 pins)

print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config 

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display 

# Clear the oled display in case it has junk on it.
oled.fill(0)           

# Add some text
# temp = str(round(temperature,2)) + " *C"
oled.text("i'm LA", Position("i'm LA"),0) 
# .text("TEXT", HORIZON_START_PIXEL, VERTICAL_START_PIXEL)
oled.text("i learn python", Position("i learn python"), 8)
oled.text("i am developer", Position("i am developer"), 16)
oled.text("i am python dev", Position("i am python dev"), 24)
oled.text('micropython IoT', Position('micropython IoT'), 32)
oled.text("raspberryPi-Pico", Position("raspberryPi-Pico"), 40)
oled.text("no way!", Position("no way!"), 48)
oled.text('128x64 display', Position('128x64 display'), 56)
utime.sleep(2)

# Finally update the oled display so the image & text is displayed
oled.show()
print('\nPrinted out')

def SayHi():
  oled.fill(0)
  oled.text('Hi there,', Position('Hi there,'), 24)
  oled.text('MicroPython is', Position('MicroPython is'), 32)
  oled.text('ready...', Position('ready...'), 40)
  oled.show()
