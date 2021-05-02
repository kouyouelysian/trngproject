'''
	TRNG PROJECT - TAKE A NOISE DATA FILE AND DRAW ITS VALUE DISTRIBUTION GRAPH
	usage: python3 analyse_ndDistributionPlot.py <filepath> <ntiers>
	ntiers is an int between 1 and 256 and is optional (default 256)
	makes sense to set it to a multiple of 8 or 16
'''

import sys
import matplotlib.pyplot as plt
import convert_noiseDataToDistribution as conv_noise

'''
	function for drawing one file's contents as a value distribution graph
	inputs are filename (path to the noise data file), tiers (nubmer of value
	groups) and graph colour
'''
def draw(fname, tiers=256, limit=1000000, col="red"):
	print("plotting by:", fname)
	data = conv_noise.convert(fname, tiers, limit)
	plt.plot(data, color=(col),label=(fname.split("/")[-1]).split(".")[0])	
	
# main run
if (__name__ == "__main__"):
	# read filename arg
	try:
		fname = sys.argv[1]
	except Exception as e:
		raise ValueError("please provide target data textfile as first argument!")
	# read and parse value limit arg
	try:
		nsamples = sys.argv[2]
	except Exception as e:
		nsamples = 1000000
	try:
		nsamples = int(nsamples)
	except Exception as e:
		raise ValueError("N of samples should be an integer! you provided:", nsamples, type(nsamples))
	# readn and parse tier
	try:
		tiers = sys.argv[3]
	except Exception as e:
		tiers = 256
	try:
		tiers = int(tiers)
	except Exception as e:
		raise ValueError("N of tiers should be an integer! you provided:", tiers, type(tiers))

	# plot graph
	ticks = [0, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 255]
	plt.xticks(ticks) #set the tick frequency on x-axis
	# set other stuff
	plt.ylim(0, 2)
	plt.ylabel('FREQUENCY') #set the label for y axis
	plt.xlabel('VALUE') #set the label for x-axis
	draw(fname, tiers, nsamples)
	plt.legend(loc="upper left")
	print("rendering...")
	plt.show() #display the graph