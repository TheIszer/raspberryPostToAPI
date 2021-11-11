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

### Main Code ###

while True:
	try:
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(TRIG,GPIO.OUT)
		GPIO.setup(ECHO,GPIO.IN)
		GPIO.output(TRIG, True)
		time.sleep(0.00001)
		GPIO.output(TRIG, False)
		 
		while GPIO.input(ECHO) == False:
			start = time.time()
		 
		while GPIO.input(ECHO) == True:
			end = time.time()
		 
		sig_time = end-start
		 
		#CM:
		distance = sig_time / 0.000058
		#inches:
		#distance = sig_time / 0.000148
		 
		print('Distance: {} centimeters'.format(distance))
		GPIO.cleanup()
		 
		
	except RuntimeError as error:
		print(error.args[0])
		time.sleep(2.0)
		continue
	
	except Exception as error:
		time.sleep(2.0)
		raise error
		
	time.sleep(5.0)