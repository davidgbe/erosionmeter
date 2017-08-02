# to communicate with NanoJet syringe created by Chemyx
from .port_driver_base import PortDriverBase

class Syringe(PortDriverBase):

	def __init__(self, port_type='usb'):
		PortDriverBase.__init__(self, port_type)

	def write(self, command):
		self.serial_port.write(bytes(command + '\r', 'ascii'))
		for line in self.serial_port.readlines():
			print(line)
