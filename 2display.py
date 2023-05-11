from machine import Pin, I2C, PWM
from i2c_lcd import I2cLcd
from time import sleep_ms

def iniLcd (n, a, l):
    i2c = I2C(n,sda=Pin(a),scl=Pin(l),freq=400000)
    devices = i2c.scan()
    print("{}".format(hex(devices[0])))
    return I2cLcd(i2c, devices[0],2, 26)
    
buzzer = PWM(Pin(15))

lcd1 = iniLcd(0, 8, 9)
lcd2 = iniLcd(1, 6, 7)

lcd1.clear()                # Clear display
text = "Hola Jairo"
lcd1.putstr(text)

lcd2.clear()                # Clear display
text = "Hola Contador"
lcd2.putstr(text)

contador = 0
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)
while True:
   reading = sensor_temp.read_u16() * conversion_factor
   temperature = 27 - (reading - 0.706)/0.001721
   strtemp = "Temp: " + str(temperature)
   lcd1.move_to(0,1)
   lcd1.putstr(strtemp)
   contador += 1
   strcontador = "Cont: " + str(contador)
   lcd2.move_to(0,1)
   lcd2.putstr(strcontador)
   sleep_ms(500)
   
   
