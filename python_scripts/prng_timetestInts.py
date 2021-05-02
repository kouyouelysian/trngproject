'''
	TRNG PROJECT - SOFTWARE ALGORITHM WORK TIME MEASURER
	gathers times of N uint32's generation for mt, urand and aes noise
	prints it to the screen

	2021
'''

# imports 

import sys
from random import *
import os
from Crypto.Cipher import AES
import time

# time calculators

def get_urand_time(n_samples = 1000):
	start_time = time.time()
	#result = os.urandom(n_samples) 
	for x in range(n_samples):
		temp = os.urandom(4) # 4 bytes for uint32
	print("URAND: %s seconds" % (time.time() - start_time))

def get_mt_time(n_samples = 1000):

	start_time = time.time()
	for x in range(n_samples):
		temp = randint(0, 4294967295) # uint32 range
	print("MT:    %s seconds" % (time.time() - start_time))

def get_aes_time(n_samples = 1000):
	# each cycle generates 16 bytes, so 4 uints per cycle
	n_samples = round(n_samples / 4) + 1

	#start of the random engine action
	out_data = bytearray()
	start_time = time.time()
	key = os.urandom(AES.block_size)
	iv = os.urandom(AES.block_size)
	message  = os.urandom(AES.block_size)
	for x in range(n_samples):
		encryptor = AES.new(key, AES.MODE_CBC, IV=iv)
		message = encryptor.encrypt(message)
		iv, message = message, iv
		out_data += message
	print("AES:   %s seconds" % (time.time() - start_time))

# main

if (__name__ == "__main__"):
	try:
		n_samples = sys.argv[1]
	except Exception as e:
		raise ValueError("please provide N of samples as first argument!")

	try:
		n_samples = int(n_samples)
	except Exception as e:
		raise ValueError("N of samples should be an integer!")

	get_urand_time(n_samples)
	get_mt_time(n_samples)
	get_aes_time(n_samples)
