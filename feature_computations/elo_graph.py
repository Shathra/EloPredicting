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

for e in elo:
	y[(int(e)-minElo)/interval] += 1

plt.plot( x, y)
plt.axis([minElo, maxElo, 0, 5000])
plt.show()