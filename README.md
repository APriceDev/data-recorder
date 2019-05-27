# Data Recorder

## Arduino

The Arduino script using TMP36 temperature sensor for data.

```C++
#include <Time.h>
#include <TimeLib.h>

// Receive data from Arduino pin A0
const int pin = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  float voltage, degreesC, degreesF, raw;

  raw = getRawData(pin);
  voltage = getVoltage(pin);

  // formulas for temp derived from (I think) Paul McMurty
  degreesC = (voltage - 0.5) * 100.0;
  degreesF = degreesC * (9.0 / 5.0) + 32.0;

  // second parameter of println '2' denotes a limit of two decimal places
  Serial.println(degreesF, 2);
  delay(1000);
}

float getRawData(int pin) {
  return (analogRead(pin));
}

float getVoltage(int pin) {
  return (analogRead(pin) * 0.004882814);
}
```

## Python

Capture temperature and timestamp data from arduino using a python script.

* import pyserial library if not already loaded

```py
pip install pyserial
```

Establish communication with Arduino and write to file.

```py
# app.py
"""
TMP36 serial com module
"""
import time
import serial

# timestamp for file name
INITIALTIMESTAMP = int(time.time() * 1000)
COM = serial.Serial('COM4', baudrate=9600, timeout=1)

with open(''.join(['data/data-', str(INITIALTIMESTAMP), '.txt']), 'a') as outfile:
    # write header
    outfile.write('time, temp\n')
    # write rows
    while True:
        SIGNAL = COM.readline().decode('ascii')
        TIMESTAMP = int(time.time() * 1000)
        outfile.write(''.join([str(TIMESTAMP), ',', SIGNAL]))
        print(TIMESTAMP, SIGNAL)
```

Remove empty lines

```py
with open('data/data-1558991081123.txt') as infile, open('data/data.txt', 'w') as outfile:
    for line in infile:
        if not line.strip():
            continue  # skip the empty line
        outfile.write(line)  # non-empty line. Write it to output
```

Read formatted txt file.

```py
import csv

with open('data/data.txt', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(f'{row[0]} {row[1]}')
```