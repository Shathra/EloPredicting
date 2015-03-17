import numpy as np
import matplotlib.pyplot as plt
import parser
import math

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

points = open("../data/stockfish.csv")

allPoints = []

i = 0;
for row in points:

	if( i == 25000):
		break

	if( row.startswith('Event')):
		continue

	matchToAdd = row.split( ",")[1].split( " ")
	matchToAdd[ len( matchToAdd) - 1] = matchToAdd[ len( matchToAdd) - 1][:-1]

	matchToAdd[:] = (value for value in matchToAdd if value != "NA" and value != "")

	matchToAdd = map( int, matchToAdd)

	allPoints.append( matchToAdd)

	i += 1

std = [0] * 25000

i = 0;
for match in allPoints:
	std[i] = stddev( match)
	i += 1


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