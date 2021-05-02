'''
	TRNG PROJECT - SOFTWARE ALGORITHM OUTPUT DATA GATHERER
	gathers results of mt, urand and aes noise generators into text files
	one line - one byte value

	2021
'''

# imports

import serial
import time
from random import *
import os
import sys
from Crypto.Cipher import AES

# functions

def acquire_mt(n_samples = 1000):
	# do plot over n samples
	n_aliveMessage = n_samples / 8
	out_data = []
	for x in range(n_samples):
		out_data.append(randint(0, 255))
		if (x % n_aliveMessage == 0):
			print("i'm still alive. MT samples generated:", x)

	f = open("mtData.txt", "a")
	f.truncate(0)
	for i in out_data:
		f.write(str(i) + "\n")
	f.close()

def acquire_urand(n_samples = 1000):
	# do plot over n samples
	n_aliveMessage = n_samples / 8
	out_data = []
	for x in range(n_samples):
		out_data.append(randint(0, 255))
		if (x % n_aliveMessage == 0):
			print("i'm still alive. URAND samples generated:", x)
	f = open("urandData.txt", "a")
	f.truncate(0)
	for i in out_data:
		f.write(str(i) + "\n")
	f.close()

def acquire_aes(n_samples = 1000):
	# do plot over n samples
	# each cycle generates 16 bytes, so
	n_samples_orig = n_samples
	n_samples = round(n_samples / 16)+1
	n_aliveMessage = round(n_samples / 8)
	out_data = bytearray()
	key = os.urandom(AES.block_size)
	iv = os.urandom(AES.block_size)
	plaintext  = os.urandom(AES.block_size)
	encryptor = AES.new(key, AES.MODE_CBC, IV=iv)
	for x in range(n_samples):
		
		ciphertext = encryptor.encrypt(plaintext)
		out_data += ciphertext
		plaintext = bytes(a ^ b for (a, b) in zip(plaintext, ciphertext))
		if (x % n_aliveMessage == 0):
			print("i'm still alive. AES samples generated: ~", x*16)
	out_data = out_data[:n_samples_orig]
	f = open("aesData.txt", "a")
	f.truncate(0)
	for i in out_data:
		f.write(str(i) + "\n")
	f.close()

# main run

if (__name__ == "__main__"):
	try:
		n_samples = sys.argv[1]
	except Exception as e:
		raise ValueError("please provide N of samples as first argument!")

	try:
		n_samples = int(n_samples)
	except Exception as e:
		raise ValueError("N of samples should be an integer!")

	acquire_mt(n_samples)
	acquire_urand(n_samples)
	acquire_aes(n_samples)
