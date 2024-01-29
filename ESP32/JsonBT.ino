#include <BluetoothSerial.h>
#include <ArduinoJson.h>

BluetoothSerial SerialBT;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("ESP32_BT"); // Nama perangkat Bluetooth
}

void loop() {
  if(SerialBT.available()){
    String receivedData = SerialBT.readStringUntil('\n');

    DynamicJsonDocument doc(1024);
    DeserializationError error = deserializeJson(doc, receivedData);

    const char* arah = doc["arah"];
    //const char* kecepatan = doc["kecepatan"];

    Serial.println(arah);
    SerialBT.println("1"); // Kirim string melalui Bluetooth
  }
}
