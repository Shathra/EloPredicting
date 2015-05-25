import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import parser
import math

results = parser.parseData( "../data/data.pgn", 50000)

data_f = open("../data/data.pgn")

'''
#----Match Quality Extraction A + B----

fd = open( "results/sum.lab", "w")

for i in range(0, len( results["whiteElo"])):
	fd.write( str( int( results["whiteElo"][i] +  results["blackElo"][i])) + "\n")

fd.close()
'''

#----Performance Difference Extraction A - B----

'''
fd = open( "results/dif.lab", "w")

for i in range(0, len( results["whiteElo"])):
    fd.write( str( int( results["whiteElo"][i] - results["blackElo"][i])) + "\n")
	#fd.write( str( abs( int( results["whiteElo"][i] - results["blackElo"][i]))) + "\n")

fd.close()
'''

'''
#----Winner Extraction cmp(A, B)----

fd = open( "results/winner.fea", "w")

for i in range(0, len( results["whiteWins"])):
	if( results["whiteWins"][i] == 1.0):
		fd.write( "1\n")

	elif( results["blackWins"][i] == 1.0):
		fd.write( "-1\n")

	elif( results["draws"][i] == 1.0):
		fd.write( "0\n")

	else:
		print( "ERROR")
		exit()

fd.close()
'''

#----Draw or Not----
'''
fd = open( "results/is_draw.fea", "w")

for i in range(0, len( results["whiteWins"])):
	if( results["whiteWins"][i] == 1.0):
		fd.write( "0\n")

	elif( results["blackWins"][i] == 1.0):
		fd.write( "0\n")

	elif( results["draws"][i] == 1.0):
		fd.write( "1\n")

	else:
		print( "ERROR")
		exit()

fd.close()


#----Match Length----

fd = open( "results/match_len.fea", "w")

length = "0"
n=50000
i = -1
for row in data_f:
    if i == n:
        break
    if row.startswith('[Site'):
    	if i >= 0:
    		fd.write( length + "\n")
    		#print( length)
        i += 1
    elif row.rfind( ".") != -1:
    	lindex = row.rfind( ".")
    	findex = row.rfind( " ", 0, lindex)
    	if findex == -1:
    		length = row[0:lindex]
    	else:
    		length = row[findex+1:lindex]

fd.write( length + "\n")

fd.close()
'''

'''
fd = open( "results/no_of_piece_taken.fea", "w")

n=50000
i = -1
no = 0;
for row in data_f:
    if i == n:
        break
    if row.startswith('[Site'):
    	if i >= 0:
    		fd.write( str(no) + "\n")
        i += 1
        no = 0;

    else:
    	no += row.count('x')
fd.write( str(no) + "\n")
fd.close()



fd1 = open( "results/no_of_piece_taken.fea")
fd2 = open( "results/match_len.fea")
fd3 = open( "results/no_of_piece_taken_scaled.fea", "w")

n=50000
i = -1
for i, row in enumerate(fd1):
	length = fd2.readline()
	length = int(length)
	result = float(row) / length
	fd3.write( str( result) + "\n")
#for i, line in enumerate(fp):

fd1.close()
fd2.close()
fd3.close()

'''

'''
fd = open( "results/no_of_checks.fea", "w")

n=50000
i = -1
no = 0;
for row in data_f:
    if i == n:
        break
    if row.startswith('[Site'):
    	if i >= 0:
    		fd.write( str(no) + "\n")
        i += 1
        no = 0;

    else:
    	no += row.count('+')

fd.write( str(no) + "\n")
fd.close()


fd1 = open( "results/no_of_checks.fea")
fd2 = open( "results/match_len.fea")
fd3 = open( "results/no_of_checks_scaled.fea", "w")

n=50000
i = -1
for i, row in enumerate(fd1):
	length = fd2.readline()
	length = int(length)
	result = float(row) / length
	fd3.write( str( result) + "\n")
#for i, line in enumerate(fp):

fd1.close()
fd2.close()
fd3.close()
'''