import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import parser
import math

results = parser.parseData( "../data/data.pgn")

data_f = open("../data/data.pgn")

#----Match Quality Extraction A + B----
'''
fd = open( "match_quality.data", "w")

for i in range(0, len( results["whiteElo"])):
	fd.write( str( int( results["whiteElo"][i] +  results["blackElo"][i])) + "\n")

fd.close()
'''

#----Performance Difference Extraction |A - B|----
'''
fd = open( "perf_diff.data", "w")

for i in range(0, len( results["whiteElo"])):
	fd.write( str( abs( int( results["whiteElo"][i] - results["blackElo"][i]))) + "\n")

fd.close()
'''

#----Winner Extraction cmp(A, B)----
'''
fd = open( "winner.data", "w")

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
fd = open( "is_draw.data", "w")

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
'''

#----Match Length----
'''
fd = open( "match_len.data", "w")

length = "0"
n=25000
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

fd.close()
'''

