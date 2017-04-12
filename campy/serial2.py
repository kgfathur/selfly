import serial

ser = serial.Serial('/dev/ttyUSB0', 57600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)

values = bytearray([4, 9, 62, 144, 56, 30, 147, 3, 210, 89, 111, 78, 184, 151, 17, 129])
ser.write(values)
