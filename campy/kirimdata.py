import serial

ser = serial.Serial('/dev/ttyUSB0', 57600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)

file = open("data.txt","r")
for line in file:
#    print '%s' % line
    ser.write("%s" % line)
file.close()
