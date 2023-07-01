import network
import time
import uiperf3

ssid =  ''
password =  ''

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting to connect:")
    time.sleep(1)

print(wlan.ifconfig())

#uiperf3.client('192.168.0.114')
uiperf3.server()
