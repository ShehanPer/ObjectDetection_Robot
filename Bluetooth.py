import serial
import time

class BluetoothConnection:
    def __init__(self, port='COM12', baudrate=9600):
        self.bluetoothSerial = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)  # Wait for the connection to initialize

    def send_data(self, data):
        self.bluetoothSerial.write(data.encode())
        time.sleep(0.1)  # Wait for data to be sent

    def close(self):
        self.bluetoothSerial.close()

def connect():
    return BluetoothConnection()

# Remember to close the connection when you're done with it
# connects.close()

