#include <BluetoothSerial.h>

BluetoothSerial SerialBT;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("ESP32_BT"); // Nama perangkat Bluetooth
}

void loop() {
  if(SerialBT.available()){
    String receivedData = SerialBT.readString();
    Serial.println(receivedData);
    SerialBT.println("1"); // Kirim string melalui Bluetooth
  }
}
