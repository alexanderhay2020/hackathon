# Servo controlled camera for hackathon

import serial
import time

ser=serial.Serial('/dev/ttyACM1',baudrate=9600)
input=[0.0,22.5,45.0,67.5,90.0]
output=[None]*5
for i in range(5):
    print 'enter angle between 0 and 90'
    #input=float(raw_input())

    # check if input is valid
    #while input<0 or input>90 or input==int:
    #            print 're-enter angle between 0 and 90'
    #        input=raw_input()

    # 992 - 1500 - 2000 . . . shortest - middle - longest in us
    print input[i]
    output2 = int(((1008*(input[i]/90))+992)*4) # 2000-992=100
    print output2
    output[i]=output2
    # input/90 gives us a percentage
    # (percentage*the range) + the minimum of the range gives us a final spot
    # *4 because we're operating in quarter microseconds (us)

    i=i+1
    #ser.write('\x84\x00'+chr(output & 127) + chr((output & 16256) >> 7))

    # compare output with a number that in binary is all 1's and all 0's
    # 127 in binary is 1111111
    # 16256 in binary is 11111110000000
    # comparing the latter you'll end up with a number xxxxxxxyyyyyyy. >> 7 shifts that to xxxxxxx
    # using chr() on those numbers outputs a string for each. add those to the servo\channel string
    # '\' add themselves into the string

for i2 in range(5):
    ser.write('\x84\x00'+chr(output[i2] & 127) + chr((output[i2] & 16256) >> 7))
    ser.write('\x84\x01'+chr(output[i2] & 127) + chr((output[i2] & 16256) >> 7))
    time.sleep(0.5)
