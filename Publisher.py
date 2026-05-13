import paho.mqtt.client as mqtt
import time
import random

BROKER = "localhost"
PORT = 1883
TOPIC = "iot/sensor/temp"

client = mqtt.Client()

client.connect(BROKER, PORT)

print("Connected to MQTT Broker!")

while True:
    temperature = random.randint(20, 35)

    message = f"Temperature: {temperature}°C"

    client.publish(TOPIC, message)

    print("Published:", message)

    time.sleep(2)
