'''
	TRNG PROJECT - DEVICE TEST CALIBRATION UTILITY
	plots the distribution of things to the console as a rough ASCII graph
	used mainly for calibration and evenity testing

	2021
'''

from trnglib import trng 
import time
from random import *
from trng_consolegraph import plotData

device = trng(portname='/dev/cu.wchusbserialfd120')
trng.connect()
trng.startStream()

# do plot over n samples
chunk_size = 4096*32
while True:
	data = []
	for x in range(chunk_size):
		data.append(int.from_bytes(trng.readStream(), "big"))
	plotData(data, tiers=64)
