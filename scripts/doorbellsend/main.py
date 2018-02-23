import network 
from machine import Pin
from mqtt import MQTTClient 
import machine 
import time 
import ubinascii

ssid = ""
wifipw = ""

mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()

print ("mac is " + mac)

# 60:01:94:1f:1b:f4 Black
# 60:01:94:25:8f:a9 Red

pin = machine.Pin(16, Pin.OUT)
button = Pin(2, Pin.IN)
pin.value(1)
time.sleep(1)
pin.value(0)
time.sleep(1)
pin.value(1)
time.sleep(1)
pin.value(0)

prevvalue = 1

pubfeed = ""
subfeed = ""

pubfeed = "makerhubevents.backdoorbell"

user = "gumakerhub"
feed = pubfeed
key = ""

 
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid,wifipw)

while not station.isconnected():  
    print("not connected")
    print(wifipw)
    print(ssid)
    time.sleep(1)
    machine.idle() 

print("Connected to Wifi\n") 

pin.value(1)
time.sleep(1)
pin.value(0)
time.sleep(1)
pin.value(1)
time.sleep(1)
pin.value(0)


 
client = MQTTClient("makerhubdoorbellnASDFQWER1", "io.adafruit.com",user=user, password=key, port=1883) 
client.connect()
client.publish(topic=user+"/feeds/" +pubfeed, msg="OFF")
pin.value(0) 

i = 0

while True: 
    if not station.isconnected():
       station.connect(ssid,wifipw)
       while not station.isconnected():  
          print("not connected")
          time.sleep(1)
          machine.idle()
       client = MQTTClient("makerhubdoorbellnASDFQWER1", "io.adafruit.com",user=user, password=key, port=1883) 
       client.connect()

    i = i + 1
    if(i % 50000 == 0):
       client.disconnect()
       time.sleep(1)
       client = MQTTClient("makerhubdoorbellnASDFQWER1", "io.adafruit.com",user=user, password=key, port=1883) 
       client.connect()       
       i = 1
    buttonval = button.value()
    if(prevvalue != buttonval and buttonval == 0):
       print("on")
       client.publish(topic=user+"/feeds/"+pubfeed, msg="ON")
    if(prevvalue != buttonval and buttonval == 1):
       client.publish(topic=user+"/feeds/"+pubfeed, msg="OFF")
       print("off")
    prevvalue = buttonval

    machine.idle()

