import socket
import json
import random
import datetime
import time

HOST = '192.168.4.1'  # Ganti dengan alamat IP ESP32
PORT = 80  # Port yang sama seperti yang digunakan di ESP32

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        arah = random.choice('ABCDE')
        #kecepatan = random.choice('OPQRSTUVW')
        
        jsonData = {"arah": arah}
        jsonString = json.dumps(jsonData)
        s.send(jsonString.encode('utf-8'))
        date = datetime.datetime.now()
        print(f"{date} -> {jsonString}")
        
        while True:
            data = s.recv(1024)
            flag = data.decode('utf-8')
            
            if flag == '1':
                arah = random.choice('ABCDE')
                #kecepatan = random.choice('OPQRSTUVW')
                
                jsonData = {"arah": arah}
                json_string = json.dumps(jsonData)
                
                s.send(json_string.encode('utf-8'))
                date = datetime.datetime.now()
                print(f"{date} -> {json_string}")

if __name__ == '__main__':
    main()
