
#include <WiFi.h>
#include <PubSubClient.h>

// Replace the SSID/Password details as per your wifi router
const char *ssid = "Butuh wifi";
const char *password = "mintamulu";

// Replace your MQTT Broker IP address here:
const char *mqtt_server = "127.0.0.1";

WiFiClient espClient;
PubSubClient client(espClient);

long lastMsg = 0;

#define ledPin 2

void blink_led(unsigned int times, unsigned int duration)
{
  for (int i = 0; i < times; i++)
  {
    digitalWrite(ledPin, HIGH);
    delay(duration);
    digitalWrite(ledPin, LOW);
    delay(200);
  }
}

void setup_wifi()
{
  delay(50);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  int c = 0;
  while (WiFi.status() != WL_CONNECTED)
  {
    blink_led(2, 200); // blink LED twice (for 200ms ON time) to indicate that wifi not connected
    delay(1000);       //
    Serial.print(".");
    c = c + 1;
    if (c > 10)
    {
      ESP.restart(); // restart ESP after 10 seconds
    }
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void connect_mqttServer()
{
  // Loop until we're reconnected
  while (!client.connected())
  {
    if (WiFi.status() != WL_CONNECTED)
    {
      setup_wifi();
    }

    Serial.print("Attempting MQTT connection...");
    if (client.connect("KRI"))
    {
      Serial.println("connected");
      client.subscribe("KRSTI/data");
    }
    else
    {
      // attempt not successful
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" trying again in 2 seconds");

      blink_led(3, 200);
      delay(2000);
    }
  }
}

// this function will be executed whenever there is data available on subscribed topics
void callback(char *topic, byte *message, unsigned int length)
{
  Serial.print("Message arrived on topic: ");
  Serial.print(topic);
  Serial.print(". Message: ");
  String messageTemp;

  for (int i = 0; i < length; i++)
  {
    Serial.print((char)message[i]);
    messageTemp += (char)message[i];
  }
  Serial.print(messageTemp);
  Serial.println();
}

void setup()
{
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);

  setup_wifi();
  client.setServer(mqtt_server, 1883); // 1883 is the default port for MQTT server
  client.setCallback(callback);
}

void loop()
{

  if (!client.connected())
  {
    connect_mqttServer();
  }
  client.loop();
}