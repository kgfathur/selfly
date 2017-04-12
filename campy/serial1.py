import sys
import glob
import serial


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """

    temp_list = glob.glob ('/dev/tty[A-Za-z]*')

    result = []
    for a_port in temp_list:
        try:
		s = serial.Serial(a_port)
		s.close()
		result.append(a_port)
        except serial.SerialException:
		pass

    return result

if __name__ == '__main__':
    print(serial_ports())
