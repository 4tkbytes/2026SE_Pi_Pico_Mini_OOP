from machine import Pin
from time import sleep

sleep(0.1) #ensure the usb is ready

# vals
led_pin = 25
led2_pin = 15

led = Pin(led_pin, Pin.OUT)
led2 = Pin(led2_pin, Pin.OUT)

while True:
    led.value(True)
    led2.value(False)
    sleep(1)
    
    led2.value(True)
    led.value(False)
    sleep(1)