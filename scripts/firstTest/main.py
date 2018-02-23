from machine import Pin
pin = Pin(16, Pin.OUT)
import time
while True:                                                                                                                  
    pin.value(0)                                                                                                             
    time.sleep(1)                                                                                                            
    pin.value(1)                                                                                                             
    time.sleep(2)
