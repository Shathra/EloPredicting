import numpy as np
import matplotlib.pyplot as plt
import parser
import math

def odd_even( list):

	odd = []
	even = []

	for i, item in enumerate( list):
		if i % 2 == 0:
			even.append( item)
		else:
			odd.append( item)

	return [odd, even]

def stddev( list):

	if( len(list) == 0):
		return 0.0

	mean = sum( list)/float(len(list))
	sumOf = 0

	for i in list:
		sumOf += ((i-mean)**2)

	return math.sqrt( sumOf/(len(list) - 1.0))

results = parser.parseData( "../data/data.pgn")
elo = np.concatenate( [results["whiteElo"], results["blackElo"]])

#points = open("../unused_files/stockfish.csv")
points = open("../data/stockfish_norm.csv")

allPoints = []

i = 0;
for row in points:

	if( i == 50000):
		break

	if( row.startswith('Event')):
		continue

	matchToAdd = row.split( ",")[1].split( " ")
	matchToAdd[ len( matchToAdd) - 1] = matchToAdd[ len( matchToAdd) - 1][:-1]

	matchToAdd[:] = (value for value in matchToAdd if value != "NA" and value != "")

	matchToAdd = map( int, matchToAdd)

	if( len(matchToAdd) == 0):
		matchToAdd = [0, 0]

	elif( len( matchToAdd) == 1):
		matchToAdd = [0, 0]

	allPoints.append( matchToAdd)

	i += 1

std = [0] * 50000

'''
fd = open( "variance_points.data", "w")
i = 0;
for match in allPoints:
	std[i] = stddev( match)
	fd.write( str(std[i]) + "\n")
	i += 1

fd.close()
'''

#Min Max values
#fd = open( "results/score_diff.data", "w")
fd1 = open( "results/min_white.data", "w")
fd2 = open( "results/max_white.data", "w")
fd3 = open( "results/min_black.data", "w")
fd4 = open( "results/max_black.data", "w")
i = 0;
for match in allPoints:
	#fd.write( str( max(match) - min(match)) + "\n")
	lis = odd_even( match)
	fd1.write( str( min( lis[0])) + "\n")
	fd2.write( str( max( lis[0])) + "\n")
	fd4.write( str( -1 * min( lis[1])) + "\n")
	fd3.write( str( -1 * max( lis[1])) + "\n")
	i += 1

fd1.close()
fd2.close()
fd3.close()
fd4.close()

'''
results = parser.parseData( "../data/data.pgn")
elo = results["whiteElo"] + results["blackElo"]
maxElo = int(max(elo))
minElo = int(min(elo))

interval = 200
noOfInterval = (maxElo-minElo)/interval + 1

x = range(minElo, maxElo, interval)
y = np.zeros( shape=(noOfInterval,1))

sumStd = np.zeros( shape=(noOfInterval,1))
no = np.zeros( shape=(noOfInterval,1))

i = 0
for dev in std:
	index = (int(elo[i])-minElo) / interval
	sumStd[index] += dev
	no[index] += 1
	i += 1

y = np.divide( sumStd, no)

plt.title( "Stockfish Points Standard Deviation Distribution")
plt.xlabel( "Total Elo Rating ( white-elo + black-elo)")
plt.ylabel( "Average Standard Deviation")
plt.plot( x, y)
plt.axis([minElo, maxElo, 0, 1000])
plt.show()
'''