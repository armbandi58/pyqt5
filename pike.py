from machine import Pin
import time

p2 = Pin(14,Pin.OUT)

p2.on()
time.sleep(10)
p2.off()
time.sleep(10)

