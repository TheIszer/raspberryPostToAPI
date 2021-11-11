'''
    Authors: Kaleb Antonio, Fernando Lopez, Alejandra Oliva, Asiel Trejo
    Emails: A01732213, A07144620,  A01731592, A01731489   @tec.mx
    Description:  Code written in python that reads the distances in a 
				  ultrasonic sensor and publishes it in an API. Use the GPIO 
                  library to get the measurements and graphql for the API. 
'''

# Body structure for a post request
# Temperature mutation
'''
mutation{
  updateComponent(name: "Ultrasonic sensor", value: "0"){
    component{
      id
      name
      value
      unit
    }
  }
}
'''
# Ultrasonic sensor
import RPi.GPIO as GPIO
import time
# Graphql
import requests

# Pins used
TRIG = 4
ECHO = 18

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
nameVarSensor4 = "Ultrasonic sensor"
valueVarSensor4 = 0                     #The value readed by the sensor4

# Token for user raspberryAdmin_1
headers = {"Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InJhc3BiZXJyeUFkbWluXzEiLCJleHAiOjE2MzY2MDcwNTksIm9yaWdJYXQiOjE2MzY2MDY3NTl9.kMkxKtWiBBKUEpBjoSG8bXS9q_URxR8GjsQCEY8_UV4"}
url = 'http://34.125.7.41:8090/graphql/'


### Main Code ###

while True:
	try:
		# Pin configuration and communication start
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(TRIG,GPIO.OUT)
		GPIO.setup(ECHO,GPIO.IN)
		GPIO.output(TRIG, True)
		time.sleep(0.00001)
		GPIO.output(TRIG, False)
		 
		# Signal time measured
		while GPIO.input(ECHO) == False:
			start = time.time()
		 
		while GPIO.input(ECHO) == True:
			end = time.time()
		 
		sig_time = end-start
		 
		# CM:
		distance = sig_time / 0.000058
		# inches:
		#distance = sig_time / 0.000148
		
		#print('Distance: {} centimeters'.format(distance))
		GPIO.cleanup()
		
		# Mutation
		valueVarSensor4 = distance
		query = 'mutation{updateComponent(name:' + f'"{nameVarSensor4}", value: "{valueVarSensor4}")' + '{component{id name value unit } }}'
		resultDistance = make_query(query, url, headers)
		
		'''distanceData = resultDistance['data']['updateComponent']['component']
		print(distanceData)
		print()'''
		
	except RuntimeError as error:
		print(error.args[0])
		time.sleep(2.0)
		continue
	
	except Exception as error:
		time.sleep(2.0)
		raise error
	
	# Try to make a post every 5 seconds
	time.sleep(5.0)
