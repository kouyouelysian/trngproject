'''
	TRNG PROJECT - CONVERT NOISE DATASET TO DIEHARD-READABLE FORMAT
	usage: python3 convert_dataFileToDiehardASCII.py <filename>
'''
import sys

'''
	main convert function
	takes in filename as argument
'''
def convert(fname):
	# open file
	try:
		f = open(fname, "r")
	except Exception as e:
		raise ValueError("no target file!")

	# read line by line
	data = []	
	for i in f:
	  data.append(int(i))
	f.close()

	# convert to new file
	newname = fname.split(".")[0]+"-diehard.txt"
	f = open(newname, "a")
	f.truncate(0)
	# iterate over each 40 bytes (10 ints per line)
	for x in range(0, len(data), 40):
		if (x+40>len(data)):
			break
		for y in range(0, 40):
			d = hex(data[x+y])[2:].upper()
			if (len(d) == 1):
				d = "0"+d
			f.write(d)
		f.write("\n")

if (__name__ == "__main__"):
	try:
		fname = sys.argv[1]
	except Exception as e:
		raise ValueError("please provide target data textfile as first argument!")

	convert(fname)
	