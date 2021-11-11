#DHT11 Sensor
import time
import board
import adafruit_dht
# Graphql
import requests

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D17)

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
      
# Body structure for a post request
queryStructure = '''
mutation{
  updateComponent(name: "DHT11-temperature", value: "0"){
    component{
      id
      name
      value
      unit
    }
  }
}
'''
#Variables
nameVarSensor1 = "DHT11-temperature"
valueVarSensor1 = 0                     #The value readed by the sensor1

# Token for user raspberryAdmin_1
headers = {"Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InJhc3BiZXJyeUFkbWluXzEiLCJleHAiOjE2MzY2MDcwNTksIm9yaWdJYXQiOjE2MzY2MDY3NTl9.kMkxKtWiBBKUEpBjoSG8bXS9q_URxR8GjsQCEY8_UV4"}
url = 'http://34.125.7.41:8090/graphql/'


### Main code ###

while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        #r = requests.post('')
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )
        
        # Mutation
        valueVarSensor1 = temperature_c
        query = 'mutation{updateComponent(name:' + f'"{nameVarSensor1}", value: "{valueVarSensor1}")' + '{component{id name value unit } }}'
        resultTemperature = make_query(query, url, headers)
        
        dht11Temperature = resultTemperature['data']['updateComponent']['component']
        print(dht11Temperature)
        print()

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
        
    # Try to make a post every 5 seconds
    time.sleep(5.0)
