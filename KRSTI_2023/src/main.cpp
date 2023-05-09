#include "slave.h"

void setup()
{
  Serial.begin(9600);
  innitWifi();
}

void loop()
{
  if (is_clientExist())
  {
    data = handleRequest(client);
    Serial.println(data);
  }
}
