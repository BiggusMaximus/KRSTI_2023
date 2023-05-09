#include <WiFi.h>
#include <HTTPClient.h>

const char *ssid = "Butuh wifi";
const char *password = "mintamulu";

void setup()
{

  Serial.begin(115200);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED)
  {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }

  Serial.println("Connected to the WiFi network");
}

void loop()
{

  if ((WiFi.status() == WL_CONNECTED))
  {

    HTTPClient http;

    http.begin("http://192.168.18.45:8090/data");
    int httpCode = http.GET();

    if (httpCode > 0)
    {

      String payload = http.getString();
      Serial.println(httpCode);
      Serial.println(payload);
    }

    else
    {
      Serial.println("Error on HTTP request");
    }

    http.end();
  }

  delay(20000);
}