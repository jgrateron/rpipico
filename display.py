from machine import I2C, Pin
from i2c_lcd import I2cLcd
from utime import sleep
import math

DEFAULT_I2C_ADDR = 0x27                         # LCD 1602 I2C address
                                                # If 0x27 doesn't respond then 0x3f is used
i2c = I2C(0,sda=Pin(4),scl=Pin(5),freq=400000) 
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR,2, 26)      # Initialize(device address, backlight settings)


def factorial(numero):
    if numero <= 0:
        return 1
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    return factorial

def elevado(n,i):
    z = 1
    for k in range(1,i+1):
        z = z * n
    return z

def calcular_pi(k):
    suma = 0
    for n in range(1,k+1):
        a1 = factorial(2*n)
        a2 = elevado(16,n)
        a3 = elevado(factorial(n),2)
        b1 = a1 / (a2 * a3)
        b2 = 1 / (2 * n + 1)
        z = b1 * b2
        suma += z
    pi = 3 * (1 + suma)
    return pi

lcd.clear()                # Clear display
text = "Hola Jairo"
lcd.putstr(text)
lcd.move_to(0,1)
sleep(1)
text = "Bienvenido..."
lcd.putstr(text)
sleep(5)
lcd.clear()
text = "Calculando pi"
lcd.putstr(text)
sleep(1)
lcd.putstr(".")
sleep(1)
lcd.putstr(".")
sleep(1)
lcd.putstr(".")
sleep(1)
lcd.move_to(0,1)
text = "Pi: " + str(calcular_pi(10)) 
lcd.putstr(text)
sleep(10)
lcd.clear()                # Clear display

