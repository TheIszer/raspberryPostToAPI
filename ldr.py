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

#Variables
nameVarSensor3 = "LDR"
valueVarSensor3 = 0                     #The value readed by the sensor3, 0 meas OFF and 1 ON

# Token for user raspberryAdmin_1
headers = {"Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InJhc3BiZXJyeUFkbWluXzEiLCJleHAiOjE2MzgzOTg5MjgsIm9yaWdJYXQiOjE2MzgzOTg2Mjh9.R-dqiYm3q-XdIG2E0-fUZVKzjC0I-iHm0nHPs5n_AN8"}
url = 'http://34.125.235.58:8081/graphql/'
### Main code ###

while True:
    if GPIO.input(LIGHT_PIN):
      valueVarSensor3 = 0
    else:
      valueVarSensor3 = 1
      
    # Mutation
    query = 'mutation{updateComponent(name:' + f'"{nameVarSensor3}", value: "{valueVarSensor3}")' + '{component{id name value unit } }}'
    resultLdr = make_query(query, url, headers)
    
    #ldrData = resultLdr['data']['updateComponent']['component']
    #print(ldrData)
    #print()
        
    # Try to make a post every 5 seconds
    time.sleep(5.0)
