# Servo controlled camera for hackathon

import serial

ser=serial.Serial('/dev/ttyACM0',baudrate=9600)

print 'enter angle between 0 and 90'
input=raw_input()

if input<0 or input>90:
    print 're-enter angle between 0 and 90'
    input=raw_input()
