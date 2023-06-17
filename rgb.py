from picozero import RGBLED
from time import sleep
import random

rgb = RGBLED(red = 2, green = 3, blue = 4)

rgb.color = (255,255,255)
sleep(1)
rgb.color = (0,255,255)
sleep(1)
rgb.color = (255,0,255)
sleep(1)
rgb.color = (255,255,0)
sleep(1)
rgb.color = (0,0,0)


for i in range(1,10):
     R=random.randint(0,255)
     G=random.randint(0,255)
     B=random.randint(0,255)
     rgb.color = (R, G, B)
     sleep(0.25)

rgb.color = (255,255,255)
