#include <WiFi.h>
#include <WebServer.h>

const char *ssid = "Butuh wifi";
const char *password = "mintamulu";
const int serverPort = 80;
String data;

WiFiServer server(serverPort);
WiFiClient client = server.available();

String urlDecode(String str)
{
    String decoded = "";
    char temp[] = "0x00";
    for (size_t i = 0; i < str.length(); i++)
    {
        char c = str.charAt(i);
        if (c == '+')
        {
            decoded += ' ';
        }
        else if (c == '%')
        {
            temp[0] = str.charAt(++i);
            temp[1] = str.charAt(++i);
            decoded += strtol(temp, NULL, 16);
        }
        else
        {
            decoded += c;
        }
    }
    return decoded;
}

String handleRequest(WiFiClient client)
{
    String request = client.readStringUntil('\r');
    String message = "";
    if (request.indexOf("/message") != -1)
    {
        if (request.indexOf("?message=") != -1)
        {
            int start = request.indexOf("?message=") + 9;
            int end = request.indexOf("HTTP") - 1;
            message = request.substring(start, end);
        }
        Serial.println("Message received: " + message);
    }

    client.println("HTTP/1.1 200 OK");
    client.println("Content-Type: text/plain");
    client.println();
    client.println("Request received.");
    return message;
}

void innitWifi()
{
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(1000);
        Serial.println("Connecting to WiFi...");
    }

    Serial.println("WiFi connected.");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());

    server.begin();
}

bool is_clientExist()
{
    client = server.available();
    if (client)
    {
        while (client.connected())
        {
            if (client.available())
            {
                return true;
            }
            else
            {
                return false;
            }
        }
    }
}