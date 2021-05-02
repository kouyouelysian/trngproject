'''
	TRNG PROJECT - FAST CONSOLE PLOT
	plots the distribution of things to the console as a rough ASCII graph
	used mainly for calibration and evenity testing

	2021
'''

glob_block = "█"
glob_halfblock = "▒"
glob_empty = " "

from random import *
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def getTierData(data, values = 256, tiers = 16):
	tierSize = values / tiers
	tierQuantities = []
	for t in range(tiers):
		tierQuantities.append(0)

	for d in data:
		tierQuantities[int(d / tierSize)] += 1

	return tierQuantities

def printPlot(tierData):
	tiers = len(tierData)
	maxQuantity = max(tierData)
	normalizedTiers = []
	for t in tierData:
		normalizedTiers.append(t*10/maxQuantity)
	for x in range(9, 0, -1):
		str = ""
		for t in range(len(normalizedTiers)):
			if (normalizedTiers[t] >= x):
				str += glob_block
			else:
				str += glob_empty
		print(str)

def plotData(data, values = 256, tiers = 16):
	t = getTierData(data, values, tiers)
	clearConsole()
	printPlot(t)

def test():
	data = []
	for x in range(256):
		data.append(randint(0, 255))
	plotData(data)

if (__name__ == "__main__"):
	test()