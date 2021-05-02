'''
	TRNG PROJECT - QUICK DIEHARD TEXT (DIEQUICK.EXE) RESULT PARSER
	this script converts the output of DIEQUICK.exe (essentialy text files)
	into useful format.
	Intended to be used by other scripts as a module, has no main function.

	2021
'''


'''
	calculates the root mean square error of a given p-values list
	relatively to an x=y line.
'''
def calc_rmse(pred, act):
	if not (len(pred) == len(act)):
		raise ValueError("something went wrong")
	error = 0
	for x in range(len(pred)):
		error += (pred[x]-act[x])*(pred[x]-act[x])
	error /= len(pred)
	error = sqrt(error)
	return error

'''
	converts results of DIEQUICK.exe into useful form
	returns [0] the list of p-values found in the file
	and [1] the root mean square error for it relatively to x=y
'''
def convert(fname):
	# open file
	try:
		f = open(fname, "r")
	except Exception as e:
		raise ValueError("no target file:", fname)

	# read line by line
	data = ["zero"]	
	for i in f:
		data.append(i)
	f.close()

	# these are hard-coded numbers of lines that contain p-values of the test
	# do. not. change them. if you use the same release i did.
	# might need adjustments if you use a different test suite, though!
	pstrings = []
	pstrings += data[2:11]+[data[17]]+[data[19]]+[data[29]]+[data[38]]
	pstrings += data[40:65]+data[77:97]+data[98:180]+data[185:187]
	pstrings += data[191:216]+data[220:230]+data[238:258]+data[263:283]
	pstrings += data[298:299]+data[301:311]+data[327:328]

	# parse p-values out of file strings
	pvalues = []
	for s in pstrings:
		pvalues.append(float("0."+s.split(".")[-1][0:4]))
	pvalues = sorted(pvalues)

	# generate ideal values, 4 digits past the dot
	idealvalues = []
	for x in range(len(pvalues)):
		idealvalues.append(round(x/len(pvalues), 4))

	# return a tuple with [0] being pvalues list and [1] being the RMSE
	return pvalues, calc_rmse(idealvalues, pvalues)
	