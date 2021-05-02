'''
	TRNG PROJECT - MULTIPLE FILES DHARD RESULT PLOTTER
	usage: python3 analyse_dhard_plot_all.py
	output: RMSE values to the console, and a graph.
	essentialy it is analyse_dhard_plot.py but without options
	and with hard-coded filenames.
'''

import sys
import matplotlib.pyplot as plt
from os.path import join
import convert_getDiehardPvals as diehard_conv 
import analyse_dhard_plot as plotter

if (__name__ == "__main__"):
	
	'''
		CAREFULLY CHECK THESE!!!
		this script does not take any external input -
		the filenames and folder with the filenames are hardcoded.

		The script expects a bunch of DIEQUICK.exe results
		(original Diehard tests battery, quick version)

	'''

	# path to the folder with quick dhard test results
	folder = "../../results/diehard_analysis/"

	# names of the files. these can be text files, binary files or whatever.
	names = [
		"URAND",
		"MT",
		"AES",
		"TRNG"
	]

	'''
		this is the rest of the program. should do just fine without
		your interventions.
	'''
	fnames = []
	for x in names:
		fnames.append(join(folder, x))

	# this is for the lines do be of different colours
	colData = [1,1,0,1,0,0,1,0,0,1,0,0]
	counter = 0

	# parse and plot each result file
	for f in fnames:
		d = diehard_conv.convert(f)
		if (f == fnames[0]):
			plotter.plot_ideal(d[0])
		print("RMSE for", names[counter],"=", d[1])
		plotter.plot(d[0], f, col=(colData[counter],colData[counter+1],colData[counter+2]))
		counter += 1
	plt.legend(loc="upper left")
	plt.show()