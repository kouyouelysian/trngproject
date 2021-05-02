'''
	TRNG PROJECT - DIEHARD QUICK TEST RESULTS PLOTTER
	usage: python3 analyse_dhard_plot.py <pathtofile>
	output: RMSE value and a graph
'''

import sys
import matplotlib.pyplot as plt
from math import sqrt
import convert_getDiehardPvals as diehard_conv

'''
	plots the given list of pvalues
	will plot absolute garbage if given anything else
	other than the diehard_conv result.
'''
def plot(pvalues, fname, col="red"):
	idealvalues = []
	for x in range(len(pvalues)):
		idealvalues.append(round(x/len(pvalues), 4))
	label = fname.split("/")[-1]
	plt.plot(pvalues, color=col,label=label)	
	
'''
	plots the ideal x=y line to compare to
'''
def plot_ideal(pvalues, col="grey"):
	plt.yticks([0,0.5,1])
	idealvalues = []
	for x in range(len(pvalues)):
		idealvalues.append(round(x/len(pvalues), 4))
	plt.plot(idealvalues, col,label="ideal")	
	
if (__name__ == "__main__"):
	# read args
	try:
		fname = sys.argv[1]
	except Exception as e:
		raise ValueError("please provide target DIEFAST.exe analysis textfile as first argument!")
	# convert and plot
	fname = fname.strip()
	d = diehard_conv.convert(fname)
	print("RMSE: ", d[1])
	plot(d[0], fname)
	plot_ideal(d[0])
	plt.legend(loc="upper left")
	plt.show() #display the graph