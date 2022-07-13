# MicroPython and IoT
# ep.4 - Firmware installation [ESP-12f(esp8266 CH340)]

# What is firmware - 003800
# [Download Firmware](https://micropython.org/download/) - 004445
# [Driver](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) - 011910
# [Driver_worked](https://www.wemos.cc/en/latest/ch340_driver.html)
# Firmware installing through command line - 201000
# LED - 022400
    - Anode (+) connect to D5 [GPIO14/HSCLK]
    - Cathode (-) connect to Ground
    ```
        from machine import Pin
        import time
        led = Pin(14, Pin.OUT)
        led.on()
        led.off()
    ```
