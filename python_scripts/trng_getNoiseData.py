'''
	TRNG PROJECT - DEVICE OUTPUT DATA GATHERER FOR N VALUES
	gathers N samples from the TRNG and puts them into a txt file
	called "deviceData.txt"
	the file is wiped before writing!!!
	if the program/the TRNG crash on execution, the file contents are
	saved up until the moment it crashed.

	2021
'''

import sys
from trnglib import trng


def getNumbers(n_samples):
	if (n_samples < 10000):
		n_aliveMessage = round(n_samples/100)
	else:
		n_aliveMessage = round(n_samples/1000)

	f = open("deviceData.txt", "a")
	f.truncate(0)

	device = trng(portname="/dev/cu.wchusbserialfd120")
	device.connect()
	device.startStream()

	for x in range(n_samples):
		f.write(str(device.readStream()) + "\n")
		if (x % n_aliveMessage == 0):
			print("i'm still alive. samples acquired:", x)

	device.stopStream()
	f.close()



if (__name__ == "__main__"):
	try:
		n_samples = sys.argv[1]
	except Exception as e:
		raise ValueError("please provide N of samples as first argument!")

	try:
		n_samples = int(n_samples)
	except Exception as e:
		raise ValueError("N of samples should be an integer!")

	getNumbers(n_samples)
