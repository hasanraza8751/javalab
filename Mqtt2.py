import time
import board
import adafruit_dht
import paho.mqtt.client as mqtt

# MQTT Setup
MQTT_BROKER = "mqtt.eclipseprojects.io"
MQTT_PORT = 1883
MQTT_TOPIC = "home/temperature"

# DHT Sensor Setup
dhtDevice = adafruit_dht.DHT22(board.D4)

# MQTT Client
client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

print("Publishing Temperature Data...")

while True:
    try:
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity

        print(f"Temp: {temperature} C  Humidity: {humidity}%")

        client.publish(MQTT_TOPIC, str(temperature))

    except RuntimeError as error:
        print(error.args[0])

    time.sleep(5)
