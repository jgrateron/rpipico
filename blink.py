from machine import Pin
import utime

led = Pin("LED", Pin.OUT)
led.value(0)

for i in range(1,100):
    led.toggle()
    utime.sleep(0.1)

led.value(0)
