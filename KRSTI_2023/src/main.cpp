#include <Arduino.h>
#include <WiFi.h>

// Replace with your network credentials
const char* ssid = "KRSTI_UPNVJ";
const char* password = "12345678";

// Replace with the IP address of your Raspberry Pi
IPAddress raspiIP(192, 168, 1, 101);
const int raspiPort = 1234;

WiFiServer server(raspiPort);

void setup() {
  Serial.begin(9600);
  
  // Connect to Wi-Fi network
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi.");
  
  // Start the TCP server
  server.begin();
  Serial.println("Server started.");
}

void loop() {
  // Check for incoming client connections
  WiFiClient client = server.available();
  if (client) {
    // Read the incoming string
    String data = client.readStringUntil('\n');
    
    // Read the incoming boolean
    byte flag = client.read();
    bool bflag = (flag == 1);
    
    // Print the received data
    Serial.print("Received: ");
    Serial.print(data);
    Serial.print(", ");
    Serial.println(bflag);
    
    // Close the client connection
    client.stop();
  }
}