import bluetooth
import random
import datetime
import time
import json

# ESP32 Bluetooth address
esp32_address = "EC:62:60:9B:E4:92"  # Replace with your ESP32's Bluetooth address

# Create a Bluetooth socket
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

# Connect to the ESP32
sock.connect((esp32_address, 1))

arah = random.choice('ABCDE')
jsonData = {"arah": arah}
jsonString = json.dumps(jsonData)
sock.send(jsonString)

date = datetime.datetime.now()
print(f"{date} -> {jsonData}")


while True:
    data = sock.recv(8)
    flag = data.decode("utf-8")
    
    if flag == "1":
        # Get keyboard input for two values
        arah = random.choice('ABCDE')
        #kecepatan = input("Masukkan Kecepatan: ")

        # Create a JSON object
        jsonData = {"arah": arah}
        #json_data = {"arah": arah, "kecepatan": kecepatan}

        # Serialize the JSON data
        json_string = json.dumps(jsonData)

        if arah == "q":
            break

        # Send the serialized JSON over Bluetooth
        sock.send(json_string)
        date = datetime.datetime.now()
        print(f"{date} -> {json_string}")

# Close the Bluetooth socket
sock.close()
