import socket
import math
import utime
import network
import time
from picozero import RGBLED
from machine import I2C, Pin
from i2c_lcd import I2cLcd

DEFAULT_I2C_ADDR = 0x27                         # LCD 1602 I2C address
                                                # If 0x27 doesn't respond then 0x3f is used
i2c = I2C(0,sda=Pin(4),scl=Pin(5),freq=400000) 
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR,2, 26)      # Initialize(device address, backlight settings)
lcd.clear()

led = Pin("LED", Pin.OUT)
led.value(0)

ssid =  ''
password =  ''

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid,password)
 
rgb = RGBLED(red = 6, green = 7, blue = 8)
rgb.color = (255,255,255)
 
# Wait for connect or fail
wait = 10
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    lcd.move_to(0,0)
    lcd.putstr('waiting for')
    lcd.move_to(0,1)
    lcd.putstr('connection...')
    print('waiting for connection...')
    time.sleep(0.5)
    lcd.move_to(0,0)
    lcd.putstr('             ')
    lcd.move_to(0,1)
    lcd.putstr('             ')
    time.sleep(0.5)
 
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('wifi connection failed')
else:
    print('connected')
    ip=wlan.ifconfig()[0]
    print('IP: ', ip)
    lcd.move_to(0,0)
    lcd.putstr(ip)
 
# Temperature Sensor
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

def url_parse(url):
    l = len(url)
    data = bytearray()
    i = 0
    while i < l:
        if url[i] != '%':
            d = ord(url[i])
            i += 1
        else:
            d = int(url[i+1:i+3], 16)
            i += 3
        data.append(d)
    return data.decode('utf8')

def temperature():
    temperature_value = sensor_temp.read_u16() * conversion_factor 
    temperature_Celcius = 27 - (temperature_value - 0.706)/0.00172169/ 8 
    return temperature_Celcius
 
def webpage(color, value):
    html = f"""
            <!DOCTYPE html>
            <html>
            <body>
            <form method="POST" action="/">
            <input type="color" value="{color}" name="color"/>
            <button type="submit">Submit</button>
            </form>
            <form method="POST" action="/">
            <button name="color" value="#FF0000">Rojo</button>
            </form>
            <form method="POST" action="/">
            <button name="color" value="#00FF00">Verde</button>
            </form>
            <form method="POST" action="/">
            <button name="color" value="#0000FF">Azul</button>
            </form>
            <form method="POST" action="/">
            <button name="color" value="#000000">Apagar</button>
            </form>  
            <p>Temperature is {value} degrees Celsius</p>
            </body>
            </html>
            """
    return html

def send(client, result, response):
    client.sendall(result + '\r\nConnection: close\r\nContent-type: text/html\r\nContent-Length: ' + str(len(response)) + '\r\n\r\n')
    client.sendall(response)
    client.close()
    print ("client close")
#end send

def serve(connection):
    while True:
        client, addr = connection.accept()
        print('client connected from', addr)
        buffer = client.recv(1024)
        data = str(buffer,'utf-8')
        array = data.split("\n")
        enviado = False
        if len(array) > 0:
            method = array[0]
            if "GET" in method:
                resource = method.split(" ")[1]
                if resource == '/favicon.ico':
                    send(client, "HTTP/1.0 404 Not Found","\r\n")
                    enviado = True
            if "POST" in method:
                for cad in array:
                    if "color" in cad:
                        try:                        
                            divcolor = url_parse(cad).split("#")
                            if len(divcolor) > 1:
                                h = divcolor[1]
                                lcd.move_to(0,1)
                                lcd.putstr(h.upper())
                                color_rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
                                rgb.color = (255 - color_rgb[0],255 - color_rgb[1], 255 - color_rgb[2])
                                value='%.2f'%temperature()
                                response=webpage("#" + h,value) + '\r\n'
                                send(client, "HTTP/1.0 200 OK",response)
                                enviado = True
                        except UnicodeError:
                            print("UnicodeError")
                        except ValueError:
                            print("ValueError")
        if not enviado:
            value='%.2f'%temperature()
            response=webpage("#ff0000",value) + '\r\n'
            send(client, "HTTP/1.0 200 OK",response)
#end serve

def open_socket(ip):
    # Open a socket
    address = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    print(connection)
    return(connection)
 
 
if ip is not None:
    connection=open_socket(ip)
    serve(connection)
