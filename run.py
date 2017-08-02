from lib.drivers.syringe import Syringe

if __name__ == '__main__':
	s = Syringe()
	s.serial_port.write(b'start')

