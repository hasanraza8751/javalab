import paho.mqtt.client as mqtt

BROKER = "192.168.1.10"   # CHANGE THIS
PORT = 1883
TOPIC = "iot/sensor/temp"

def on_connect(client, userdata, flags, rc):
    print("Connected to Broker!")

    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print("Received:", msg.payload.decode())

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT)

print("Waiting for messages...")

client.loop_forever()
