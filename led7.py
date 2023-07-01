from machine import Pin
import utime

def displayNumero(numero, leds):
    for i in range(0,7):
        if numero[i] == True:
            leds[i].off()
        else:
            leds[i].on()
    
led_a = Pin(19, Pin.OUT)    
led_b = Pin(18, Pin.OUT)   
led_c = Pin(15, Pin.OUT)
led_d = Pin(6, Pin.OUT)
led_e = Pin(2, Pin.OUT)
led_f = Pin(20, Pin.OUT)
led_g = Pin(21, Pin.OUT)

leds =   [led_a, led_b, led_c, led_d, led_e, led_f, led_g]
uno    = [False, True,  True,  False, False, False, False]
dos    = [True,  True,  False, True,  True,  False, True]
tres   = [True,  True,  True,  True,  False, False, True]
cuatro = [False, True,  True,  False, False, True,  True]
cinco  = [True,  False, True,  True,  False, True,  True]
seis   = [True,  False, True,  True,  True,  True,  True]
siete  = [True,  True,  True,  False, False, True,  False]
ocho   = [True,  True,  True,  True,  True,  True,  True]
nueve  = [True,  True,  True,  True,  False,  True, True]
cero   = [True,  True,  True,  True,  True,  True,  False]

numeros = [uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve,cero]

for led in leds:
    led.on()

while True:
    for number in numeros:
        displayNumero(number, leds)
        utime.sleep(2)    

for led in leds:
    led.on()
