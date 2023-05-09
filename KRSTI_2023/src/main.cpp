#include <WiFi.h>

const char *ssid = "Butuh wifi";
const char *password = "mintamulu";

IPAddress serverIP(192, 168, 18, 168); // IP address of the Raspberry Pi
const int serverPort = 5005;           // port number to use

void setup()
{
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println(WiFi.localIP());
  Serial.println("Connected to WiFi");
}

void loop()
{
  // wait for data from the Raspberry Pi
  if (Serial.available() > 0)
  {
    // read the incoming data
    String data = Serial.readString();
    Serial.println("Received data: " + data);
  }
}