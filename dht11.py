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

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)
