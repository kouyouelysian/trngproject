'''
	TRNG PROJECT - DEVICE N 32BIT UNSIGNED INTS GENERATION TIME MEASURE SCRIPT
	usage: python3 trng_timetestInts.py <int n samples>
	2021
'''

import sys
from trnglib import trng
import time

def get_trng_time(n_samples = 1000):
	device = trng(portname="/dev/cu.wchusbserialfd120")
	device.connect()
	start_time = time.time()
	device.startStream()
	for x in range(n_samples):
		temp = device.readStreamInt()
	device.stopStream()
	print("TRNG: %s seconds" % (time.time() - start_time))



if (__name__ == "__main__"):
	try:
		n_samples = sys.argv[1]
	except Exception as e:
		raise ValueError("please provide N of samples as first argument!")

	try:
		n_samples = int(n_samples)
	except Exception as e:
		raise ValueError("N of samples should be an integer!")

	get_trng_time(n_samples)
