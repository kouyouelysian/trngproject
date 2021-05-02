'''
	TRNG PROJECT - TAKE NOISE DATA FILES AND DRAW THEIR VALUE DISTRIBUTION
	ON THE SAME GRAPH
	usage: python3 analyse_ndDistributionPlot-ALL.py <nsamples> <ntiers>
	ntiers is an int between 1 and 256 and is optional (default 256)
	
	makes sense to set it to a multiple of 8 or 16
	nsamples is the maximum numble of sample values to take into account 
	is also optional (default 1000000 - one million)
	
	essentialy it is analyse_ndDistributionPlot.py but with a nsamples arg
	and with hard-coded filenames.
'''

import sys
import matplotlib.pyplot as plt
import numpy
from os.path import join

import analyse_ndDistributionPlot as plotter

if (__name__ == "__main__"):

	# read options
	try:
		nsamples = sys.argv[1]
	except Exception as e:
		nsamples = 1000000

	try:
		nsamples = int(nsamples)
	except Exception as e:
		raise ValueError("N of samples should be an integer! you provided:", nsamples, type(nsamples))

	try:
		tiers = sys.argv[2]
	except Exception as e:
		tiers = 256

	try:
		tiers = int(tiers)
	except Exception as e:
		raise ValueError("N of tiers should be an integer! you provided:", tiers, type(tiers))

	'''
		CAREFULLY CHECK THESE!!!
		this script does not take any external input -
		the filenames and folder with the filenames are hardcoded.

		The script expects results of prng_getNoiseData or trng_getNoiseData
	'''
	# folder with target files
	folder = "../../results/noisedata/"
	# filenames
	names = [
		"URAND.txt",
		"MT.txt",
		"AES.txt",
		"TRNG.txt"
		
	]
	# make filenames
	fnames = []
	for x in names:
		fnames.append(join(folder, x))

	# setup the plot
	colors=["lime","yellow","cyan","red"]
	ticks = [0, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 255]
	plt.xticks(ticks)
	plt.ylim(0, 2)
	plt.ylabel('FREQUENCY')
	plt.xlabel('VALUE')
	# plot all noise data files' distributions
	fcount = 0
	for fname in fnames:
		plotter.draw(fname, tiers, nsamples, colors[fcount])
		fcount += 1
	plt.legend(loc="upper left")
	print("rendering...")
	plt.show()
