from machine import Pin, I2C,PWM
from i2c_lcd import I2cLcd
from time import sleep_ms
import utime

def iniLcd (n, a, l):
    i2c = I2C(n,sda=Pin(a),scl=Pin(l),freq=400000)
    devices = i2c.scan()
    print("{}".format(hex(devices[0])))
    return I2cLcd(i2c, devices[0],2, 26)

def sound (buzzer,tones):
    for tone in tones:
        buzzer.freq(tone[0])
        buzzer.duty_u16(1000)
        sleep_ms(tone[1])

def lcd_show(lcd,x,y,text):
    lcd.move_to(x,y)
    lcd.putstr(text)

buzzer = PWM(Pin(15))
busy = [[913,274],[1428,380],[1776,380]]

lcd = iniLcd(0, 8, 9)

lcd.clear()
text = "Hola Jairo"
lcd.putstr(text)

trig = Pin(2, Pin.OUT)
echo = Pin(3, Pin.IN)
trig.value(0)
sonido = False

while True:
    trig.value(1)
    utime.sleep_us(10)
    trig.value(0)
    t1 = utime.ticks_us()
    while echo.value() == 0:
        t1 = utime.ticks_us()
    while echo.value() == 1:
        t2 = utime.ticks_us()
    t = t2 - t1
    d = 17 * t / 1000
    if d < 20:
        lcd_show(lcd,0,0,"Alejate! Peligro")
        if sonido == False:
            sonido = True
            sound(buzzer,busy)
            buzzer.duty_u16(0)
    else:
        lcd_show(lcd,0,0,"Hola Jairo      ")
        sonido = False

    distancia = "Distancia: {} cm".format(d)
    lcd.move_to(0,1)
    lcd.putstr(distancia)
    utime.sleep(1)
