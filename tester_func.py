#!/usr/bin/python

def test( test_path, validation_path):

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
		return [-1,-1]

	mse = 0
	rss = 0

	total = 0

	for i in xrange( len(test)):
		rss += pow( validation[i] - test[i], 2.0)
		total += abs( validation[i] - test[i])

	mse = rss / len(test)
	err = total / len(test)

	test_fd.close()
	validation_fd.close()

	return [ err, mse]