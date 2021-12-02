'''
    Authors: Kaleb Antonio, Fernando Lopez, Alejandra Oliva, Asiel Trejo
    Emails: A01732213, A07144620,  A01731592, A01731489   @tec.mx
    Description:    Code written in python that reads the value from an API
                    and use an actuator. Use graphql for the API. 
'''

# Body structure for a post request
# LED mutation
'''
query{
  components{
    id
    name
    cType
    value
    unit
    owner {
      id
    }
  }
}
'''

# LED
import RPi.GPIO as GPIO
import time
# Graphql
import requests
# Json
import json

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

# Initial the LED device, with data pin connected to 24
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LED_PIN = 24
GPIO.setup(LED_PIN, GPIO.OUT)

#Variables
nameVarActuator1 = "LED"
valueVarActuator1 = 0                     #The value readed by the sensor3, 0 meas OFF and 1 ON

# Token for user raspberryAdmin_1
headers = {"Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InJhc3BiZXJyeUFkbWluXzEiLCJleHAiOjE2MzgzOTg5MjgsIm9yaWdJYXQiOjE2MzgzOTg2Mjh9.R-dqiYm3q-XdIG2E0-fUZVKzjC0I-iHm0nHPs5n_AN8"}
url = 'http://34.125.235.58:8081/graphql/'


### Main code ###
while True:
    # Query
    query = 'query{components{id name cType value unit owner{id}}}'
    queryResult = make_query(query, url, headers)   
    queryComponentsList = queryResult['data']['components']
    
    # Filter python objects with list comprehensions, for actuator1
    ledDataList = [x
       for x in queryComponentsList
       if x['name'] == nameVarActuator1
    ]
    
    if ledDataList[0]['value'] == '0':
        GPIO.output(LED_PIN, False)
    elif ledDataList[0]['value'] == '1':
        GPIO.output(LED_PIN, True)
    
    # Try to make a query every 5 seconds
    time.sleep(5.0)
