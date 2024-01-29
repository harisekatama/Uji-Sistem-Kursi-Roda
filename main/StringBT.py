import bluetooth
import random
import datetime
import time

# Cari perangkat Bluetooth
nearby_devices = bluetooth.discover_devices()

# Ambil alamat MAC dari ESP32 (pastikan sudah dipasangkan sebelumnya)
esp32_address = "C0:49:EF:E7:BD:EA"  # Ganti dengan alamat MAC ESP32 yang sesuai

# Lakukan koneksi
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((esp32_address, 1))

arah = random.choice('ABCDE')
kecepatan = random.choice('OPQRSTUVW')
pesan = f"{arah},{kecepatan}"
sock.send(pesan)

date = datetime.datetime.now()
print(f"{date} -> {pesan}")

i = 0

# Terima data
while True:
    data = sock.recv(8)
    flag = data.decode("utf-8")
    #print("Received:", flag)
    
    if flag == '1':
        arah = random.choice('ABCDE')
        kecepatan = random.choice('OPQRSTUVW')
        pesan = f"{arah},{kecepatan}"
        i = i + 1
        
        if arah == 'q' or i == 10:
            break
        
        sock.send(pesan)
        date = datetime.datetime.now()
        print(f"{date} -> {pesan}")
        
# Tutup koneksi
sock.close()
