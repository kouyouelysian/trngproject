'''
	TRNG PROJECT - DEMO PROGRAM: SIMPLE TEST
	usage: python3 demo_simpletest.py
	
	connects to the trng
	gets one random byte, one random uint32 and a stream of 16 random bytes
	disconnects from the trng

	2021
'''
from trnglib import trng
from time import sleep

# setup and connect the TRNG
print("")
device = trng(portname='/dev/cu.wchusbserialfd120')
device.connect()
sleep(1)

# byte read
print("\ngetting a random byte from TRNG")
v = device.getRandomByte()
print("got value:", v)
sleep(1)

# int read
print("\ngetting a random 32-bit integer from the TRNG")
v = device.getRandomInt()
print("got value:", v)
sleep(1)

# print stream of bytes
print("\nsetting the device to byte stream mode and printing 16 random bytes")
device.startStream()
for x in range(16):
	v = device.readStream()
	print("value #", x, ":", v)
device.stopStream()
sleep(1)

# disconnect
print("")
device.disconnect()
print("")
sleep(1)
