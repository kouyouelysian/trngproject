'''
	TRNG PROJECT - INTERFACE LIBRARY
	a library to facilitate the connection to the arduino-based TRNG

	2021
'''

# imports

import serial
from time import sleep

# internal vars

class trng:

	'''
	class instance initializer
	'''
	def __init__(self, portname, verbose=True):
		self.portname = portname
		self.verbose = verbose
		self.connection = None
	
	'''
	tries establishing connection to the port PORTNAME
	returns True on success and False (and a printed warning) on failure
	'''
	def connect(self):
		if (self.verbose):
			print("Trying to connect to the TRNG device...")
		try:
			self.connection = serial.Serial(
				port=self.portname,
				baudrate=115200,
			    bytesize=serial.EIGHTBITS,
			)
			
		except Exception as e:
			if (self.verbose):
				print("TRNG connection failed! error:", e)
			return False
		sleep(2)
		if not self.connection.is_open:
			self.connection.open()
		if (self.verbose):
			print("TRNG connection successful!")
		return True

	'''
	disconnects the device
	'''
	def disconnect(self):
		self.sendOption(b"D")
		print("Trying to disconnect to the TRNG device...")
		sleep(1)
		if (not self.connection == None):
			self.connection.close()
			if (self.verbose):
				print("device disconnected successfully.")
		else:
			if (self.verbose):
				print("device not connected!")

	'''
	checks if the connection is there
	'''
	def checkConnection(self):
		if (self.connection == None):
			raise ValueError("device not connected!")
			return False
		return True

	'''
	sends one character of message to the device
	message is a string, only the first letter of it matters
	ignores case
	'''
	def sendOption(self, message):
		if (self.checkConnection()):
			self.connection.write(message)
		else:
			if (self.verbose):
				print("device not connected!")

	'''
	sets the TRNG into S(tream) mode
	'''
	def startStream(self):
		self.sendOption(b"S")
	'''
	stops the TRNG's S(tream) mode with the E(nough) command
	'''
	def stopStream(self):
		self.sendOption(b"E")


	'''
	gets one single random byte from the trng
	returns it as an INTEGER
	'''
	def getRandomByte(self):
		self.sendOption(b"B")
		val = self.connection.read()
		return int.from_bytes(val, "big")


	'''
	gets N random bytes from the trng
	'''
	def getRandomBytesArray(self,n):
		if (self.checkConnection()):
			self.startStream()
			bytes = bytearray()
			for x in range(n):
				val = self.connection.read()
				bytes += val
			self.stopStream()
			return bytes




	'''
	gets a random unsigned 32bit integer
	'''
	def getRandomInt(self):
		if (self.checkConnection()):
			bytes = bytearray()
			for x in range(4):
				self.sendOption(b"B")
				val = self.connection.read()
				bytes += val
			randint = int.from_bytes(bytes, "big")
			return randint

	'''
	reads whatever is on the serial
	is to be used after startStream
	use stopStream after you're done with it
	returns its decimal value as a python integer
	'''
	def readStream(self):
		val = self.connection.read()
		return int.from_bytes(val, "big")


	'''
	same as above but as a single element python bytes array
	'''
	def readStreamAsBytes(self):
		if (self.checkConnection()):
			val = self.connection.read()
			return val

	'''
	reads whatever is on the serial 4 times
	makes a 32bit uint out of that
	is to be used after startStream
	use stopStream after you're done with it
	'''
	def readStreamInt(self):
		if (self.checkConnection()):
			bytes = bytearray()
			for x in range(4):
				val = self.connection.read()
				bytes += val
			randint = int.from_bytes(bytes, "big")
			return randint
			