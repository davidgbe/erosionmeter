import serial # https://pythonhosted.org/pyserial
from serial.tools import list_ports

class PortDriverBase:

	def __init__(self, port_type):
		# find ports of specified type
		ports_of_type = list(list_ports.grep(port_type))
		if len(ports_of_type) == 0:
			raise RuntimeError('No port names matched provided keyword')
		port_name = ports_of_type[0][0]
		# by default, has baudrate 9600, bytesize 8, stop bits 1
		self.serial_port = serial.Serial(port_name)
		self.serial_port.timeout = 2

	def __del__(self):
		if self.serial_port.is_open:
			self.serial_port.close()
