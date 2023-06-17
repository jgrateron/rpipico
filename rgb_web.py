from picozero import RGBLED
from time import sleep
import random
import network
import socket

rgb = RGBLED(red = 2, green = 3, blue = 4)

rgb.color = (0,255,255)
sleep(1)

ssid =  'intermg'
password =  'lauracamila3'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    sleep(1)

# Handle connection error

if wlan.status() != 3:
    raise RuntimeError('network connection failed')

else:print('Connected')

status = wlan.ifconfig()
print( 'ip = ' + status[0] )

rgb.color = (255,255,255)

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print('listening on', addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    R=random.randint(0,255)
    G=random.randint(0,255)
    B=random.randint(0,255)
    rgb.color = (R, G, B)
    response = "<html><body><H1>Hola desde Raspberrypi Pico</H1></body></html>\r\n"
    cl.sendall('HTTP/1.0 200 OK\r\nConnection: close\r\nContent-type: text/html\r\nContent-Length: ' + str(len(response)) + '\r\n\r\n')
    cl.sendall(response)
    sleep(1)
    cl.close()
