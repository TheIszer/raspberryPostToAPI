import RPi.GPIO as GPIO
import time
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
