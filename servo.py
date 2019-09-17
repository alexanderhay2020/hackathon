# Servo controlled camera for hackathon

import serial
import time

ser=serial.Serial('/dev/ttyACM2',baudrate=9600)

# calib=3968 # 0 degree angle
calib=5984 # 45 degree angle
# calib=8000 # 90 degree angle
print calib

ser.write('\x84\x00'+chr(calib & 127) + chr((calib & 16256) >> 7))
ser.write('\x84\x01'+chr(calib & 127) + chr((calib & 16256) >> 7))

# sets servos to calib value
print 'set step'
step=int(raw_input())
place=5984

def arrow():

    print 'arrow'
    input=str(raw_input())
    print input
    global place

    if input=='\x1b[A': #up
        print 'up'
        place=place+step
        ser.write('\x84\x01'+chr(place & 127) + chr(((place & 16256) >> 7)))
    if input=='\x1b[B': #down
        print 'down'
        place=place-step
        ser.write('\x84\x01'+chr(place & 127) + chr(((place & 16256) >> 7)))
    if input=='\x1b[D': #left
        print 'left'
        place=place+step
        ser.write('\x84\x00'+chr(place & 127) + chr(((place & 16256) >> 7)))
    if input=='\x1b[C': #right
        print 'right'
        place=place-step
        ser.write('\x84\x00'+chr(place & 127) + chr(((place & 16256) >> 7)))

while True:
    arrow()
