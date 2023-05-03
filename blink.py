from machine import Pin
import utime

led = Pin("LED", Pin.OUT)
led.value(0)

for i in range(1,10):
    led.toggle()
    utime.sleep(1)

led.value(0)
