import time
import Adafruit_DHT
import paho.mqtt.client as mqtt

# MQTT Broker setup
MQTT_BROKER = "mqtt.eclipseprojects.io"
MQTT_PORT = 1883
MQTT_TOPIC = "home/temperature"

# DHT Sensor setup
DHT_SENSOR = Adafruit_DHT.DHT22   # Use DHT11 if you have DHT11
DHT_PIN = 4                       # GPIO4

# Create MQTT client
client = mqtt.Client()

# Connect callback
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with result code", rc)

client.on_connect = on_connect

# Connect to broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Start MQTT loop
client.loop_start()

# Main loop
while True:

    # Read data from sensor
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:

        print(f"Temperature: {temperature:.1f}°C  Humidity: {humidity:.1f}%")

        # Publish temperature
        client.publish(MQTT_TOPIC, f"Temperature: {temperature:.1f}°C")

    else:
        print("Failed to retrieve data from DHT sensor")

    time.sleep(10)
