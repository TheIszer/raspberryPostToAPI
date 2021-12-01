'''
    Authors: Kaleb Antonio, Fernando Lopez, Alejandra Oliva, Asiel Trejo
    Emails: A01732213, A07144620,  A01731592, A01731489   @tec.mx
    Description:    Code written in python that reads the value from an API
                    and use an actuator. Use graphql for the API. 
'''
# LED
import RPi.GPIO as GPIO
import time
# Graphql
import requests

# Initial the LED device, with data pin connected to 24
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LED_PIN = 24
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
    GPIO.output(LED_PIN, True)
    time.sleep(5.0)
    GPIO.output(LED_PIN, False)
    time.sleep(5.0)
