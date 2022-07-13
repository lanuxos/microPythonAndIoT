# MicroPython and IoT
# ep.3 - Basic Python, Fritzing

# Fritzing - 001715 
    - Basic circuit - 010330
    - LED pin
        - Cathode [-], shorter, bigger
        - Anode [+], longer, smaller
# Python condition [if-else] - 014700
# MicroPython blink LED - 022130
    - ADC - analog to digital converter
    ```
        import machine
        import time
        import pyb

        # Y12 - LED
        # Y4 - ADC [0-255]

        LED = machine.Pin('Y12')

        LED.on()
        time.sleep(3)
        LED.off()

        ADC_PIN = machine.Pin('Y4')
        ADC = pyb.ADC(ADC_PIN)
        print('ADC Value: ', ADC.read())

        while True:
            if ADC.read() < 50:
                LED.off()
            elif ADC.read() < 100:
                LED.on()
                time.sleep(0.5)
                LED.off()
                time.sleep(0.5)
            else:
                LED.on()
    ```