import numpy as np
import matplotlib.pyplot as plt
import parser

results = parser.parseData( "data.pgn")
elo = np.concatenate( [results["whiteElo"], results["blackElo"]])
maxElo = int(max(elo))
minElo = int(min(elo))

interval=50;
noOfInterval = (maxElo-minElo)/interval + 1

x = range(minElo, maxElo, interval)
y = np.zeros( shape=(noOfInterval,1))



hist, bins = np.histogram( elo, bins=50)
width=0.7*(bins[1] - bins[0])
center=(bins[:-1] + bins[1:]) / 2

plt.title( "Elo Rating Distribution")
plt.xlabel( "Elo Ratings")
plt.ylabel( "Number of Players")
plt.bar( center, hist, align="center", width=width)
plt.show()
