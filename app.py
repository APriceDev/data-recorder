"""
TMP36 serial com module
"""
import time
import serial
# import csv

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
        # outfile.close()
        print(TIMESTAMP, SIGNAL)
