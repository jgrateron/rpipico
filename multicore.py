import _thread, utime
from machine import Pin

SLEEP = 0.030
MAX = 50

def task():
    led = Pin("LED", Pin.OUT)
    led.value(0)
    for i in range(1,MAX):
        led.toggle()
        utime.sleep(SLEEP)
    led.value(0)

_thread.start_new_thread(task,())

for i in range(1,MAX):
    print(i)
    utime.sleep(SLEEP)
