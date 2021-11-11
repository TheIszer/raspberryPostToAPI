# LDR sensor
import RPi.GPIO as GPIO
import time
# Graphql
import requests

# Initial the dht device, with data pin connected to 23
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LIGHT_PIN = 23
GPIO.setup(LIGHT_PIN, GPIO.IN)

while True:
    if GPIO.input(LIGHT_PIN):
      print ('NO HAY LUZ')
    else:
      print ('LUZ') 
    time.sleep(1)
