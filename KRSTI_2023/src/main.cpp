#include <Arduino.h>

#define KY_ANALOG A0
#define KY_DIGITAL 7

void setup()
{
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(KY_ANALOG, INPUT);
  pinMode(KY_DIGITAL, INPUT);
}

void loop()
{
  // put your main code here, to run repeatedly:
  int val = analogRead(KY_ANALOG);
  Serial.println(
      "ANALOG : " + String(val) +
      " | DIGITAL : " + String(digitalRead(KY_DIGITAL)));
}