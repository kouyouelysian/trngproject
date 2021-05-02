'''
	TRNG PROJECT - NOISE DATA VISUALISER
	usage: python3 analyse_dataToImage.py targetDataTxt.txt <values per side, int> <scale factor, int>
	scale is optional! defaults to 1
'''

import sys
from PIL import Image

def test():
	img = Image.new( 'RGB', (255,255), "black") # Create a new black image
	pixels = img.load() # Create the pixel map
	for i in range(img.size[0]):    # For every pixel:
	    for j in range(img.size[1]):
	        pixels[i,j] = (i, j, 100) # Set the colour accordingly
	img.show()

def get_thresh(data, side, name, scale=1, thresh=128):
	counter = 0
	img = Image.new( 'RGB', (side,side), "black") # Create a new black image
	pixels = img.load() # Create the pixel map
	for i in range(img.size[0]):    # For every pixel:
		for j in range(img.size[1]):
			val = data[counter]
			if (val > thresh):
				val = 255
			else:
				val = 0
			pixels[i,j] = (val,val,val) # Set the colour accordingly
			counter += 1

	newsize = (side*scale, side*scale)
	img = img.resize(newsize, Image.NEAREST)
	img.save(oname + "-threshold.png")

def get_greyscale(data, side, name, scale=1):
	counter = 0
	img = Image.new( 'RGB', (side,side), "black") # Create a new black image
	pixels = img.load() # Create the pixel map
	for i in range(img.size[0]):    # For every pixel:
		for j in range(img.size[1]):
			pixels[i,j] = (data[counter], data[counter], data[counter]) # Set the colour accordingly
			counter += 1
	newsize = (side*scale, side*scale)
	img = img.resize(newsize, Image.NEAREST)
	img.save(oname + "-greyscale.png")


if (__name__ == "__main__"):
	# get args
	try:
		fname = sys.argv[1]
	except Exception as e:
		raise ValueError("please provide name of the target txt file with values as first argument!")
	try:
		f = open(fname, "r")
	except Exception as e:
		raise ValueError("unable to open txt file!")
	try:
		side = sys.argv[2]
	except Exception as e:
		raise ValueError("please provide picture side size as second argument!")
	try:
		side = int(side)
	except Exception as e:
		raise ValueError("picture side size should be an integer!")
	try:
		scale = sys.argv[3]
	except Exception as e:
		scale = 1
	try:
		scale = int(scale)
	except Exception as e:
		raise ValueError("scale should be an integer!")

	# read data

	data = []
	lines_read = 0
	for i in f:
		data.append(int(i))
		if (lines_read == side*side+1):
			break
		lines_read += 1

	# process
	oname = (fname.split("/")[-1]).split(".")[0]
	get_greyscale(data, side, oname, scale)
	get_thresh(data, side, oname, scale)
