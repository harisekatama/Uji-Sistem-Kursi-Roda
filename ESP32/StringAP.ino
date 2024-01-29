#include <WiFi.h>
#include <Arduino.h>

const char* ssid = "B300Lab_ESP32"; // Nama SSID untuk Access Point
const char* password = "123123123"; // Password untuk Access Point

WiFiServer server(80); // Menggunakan port 80 untuk koneksi

void setup() {
  Serial.begin(115200);
  delay(1000);

  // Mulai menghubungkan ke Access Point yang dibuat oleh ESP32
  WiFi.softAP(ssid, password);
  delay(100);

  server.begin(); // Memulai server
  Serial.println("Server started");
}

void loop() {
  WiFiClient client = server.available(); // Cek koneksi dari client

  if (client) { // Jika ada koneksi dari client
    Serial.println("New client connected");
    
    while (client.connected()) {
      while (client.available()) {
        String receivedData = client.readStringUntil('\n');
        Serial.println(receivedData);
        client.print("1");
      }
    }
    
    client.stop(); // Hentikan koneksi client
    Serial.println("Client disconnected");
  }
}
