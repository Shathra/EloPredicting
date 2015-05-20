#Tester script to find MSE and RSS error rates of a model

import sys

def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)

if( len(sys.argv) < 3):
	print "Usage: test_path validation_path"
	exit()

test_path = str(sys.argv[1])
validation_path = str(sys.argv[2])

test_fd = open( test_path)
validation_fd = open( validation_path)

test = []
validation = []

for i, row in enumerate( test_fd):
	if hasNumbers(row):
		test.append( float(row))

for i, row in enumerate( validation_fd):
	if hasNumbers(row):
		validation.append( float(row))

if( len(test) != len(validation)):
	print "Numbers are different"
	exit()

mse = 0
rss = 0

for i in xrange( len(test)):
	rss += pow( validation[i] - test[i], 2.0)

mse = rss / len(test)

print( "Mean squared error (MSE) is " + str(mse))
print( "Residual sum of squares error (RSS) is " + str(rss))

test_fd.close()
validation_fd.close()