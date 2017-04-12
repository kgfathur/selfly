import serial

ser = serial.Serial('/dev/ttyACM0', 57600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)

while True:
    a=ser.readline()
    print("%s" % a)
