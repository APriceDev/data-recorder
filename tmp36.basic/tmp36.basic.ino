#include <Time.h>
#include <TimeLib.h>

const int pin = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  float voltage, degreesC, degreesF, raw;

  raw = getRawData(pin);
  voltage = getVoltage(pin);
  degreesC = (voltage - 0.5) * 100.0;
  degreesF = degreesC * (9.0 / 5.0) + 32.0;
//  Serial.println(raw);
//  Serial.print("voltage: ");
//  Serial.print(voltage);
//  Serial.print(" deg C: ");
//  Serial.print(degreesC);
//  Serial.print(" deg F: ");
    
    Serial.println(degreesF, 2);
//  Serial.print(" ");
//  Serial.println(now());

  delay(1000);
}

float getRawData(int pin) {
  return (analogRead(pin));
}

float getVoltage(int pin) {
  return (analogRead(pin) * 0.004882814);
}
