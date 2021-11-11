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

# Function to make a post to graphql 
def make_query(query, url, headers):
    """
    Make query response
    """
    request = requests.post(url, json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

while True:
    if GPIO.input(LIGHT_PIN):
      print ('NO HAY LUZ')
    else:
      print ('LUZ') 
    time.sleep(1)
