# Servo controlled camera for hackathon

import serial

#ser=serial.Serial('/dev/ttyACM0',baudrate=9600)

print 'enter angle between 0 and 90'
input=float(raw_input())

# check if input is valid
#while input<0 or input>90 or input==int:
#            print 're-enter angle between 0 and 90'
#        input=raw_input()

# 992 - 1500 - 2000 . . . shortest - middle - longest in us

output = ((1008*(input/90))+992)*4 # 2000-992=1008

# input/90 gives us a percentage
# (percentage*the range) + the minimum of the range gives us a final spot
# *4 because we're operating in quarter microseconds (us)


#lowerbits='0'+'str(bin(int(output)))[-7:]
bits=str(bin(int(output)))[2:]
lowerbits='0'+bits[-7:]
# int() to give bin() a proper argument
# convert bin to a string
# call for the last 7 digits
# insert a '0' at the beginning of the string
# lowerbits='0'+(str(bin(int(output)))[2:])[-7:] # does it all in one line

upperbits=bits[:(len(bits)-7)] # retrieves the first bits not called from lower lowerbits

hexlb=hex(int(lowerbits,2))[1:] # produces a string of the hex value to pass to .write
hexub=hex(int(upperbits,2))[1:] #same thing

for prefix in range(8-len(upperbits)):
    upperbits='0'+upperbits

    # adds 0's to upperbits to prep for hex conversion

print output

ser.write('\x84\x00\x40\x3E')
