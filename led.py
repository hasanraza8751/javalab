from bluedot.btcomm import BluetoothServer
from signal import pause
import RPi.GPIO as GPIO

# GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

LED_PIN = 3   # Change if your wiring is different
GPIO.setup(LED_PIN, GPIO.OUT)

# Function to handle received data
def data_received(data):
    data = data.strip()
    print("Received:", data)

    if data == "led_on":
        GPIO.output(LED_PIN, GPIO.HIGH)

    elif data == "led_off":
        GPIO.output(LED_PIN, GPIO.LOW)

    else:
        print("Wrong Command")

# Start Bluetooth server
server = BluetoothServer(data_received)

print("Waiting for Bluetooth connection...")

pause()