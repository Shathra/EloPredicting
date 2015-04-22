import numpy as np
import matplotlib.pyplot as plt

'''
n=2500
file_x = "is_draw.data"

match_quality = np.loadtxt( 'match_quality.data')
data_x = np.loadtxt( file_x)

plt.scatter(data_x[:n], match_quality[:n], marker='.', c='r')
plt.xlabel( file_x)
plt.ylabel('Match Quality (A+B)')
plt.show()
'''

file_x = "is_draw.data"

match_quality = np.loadtxt( 'match_quality.data')
data_x = np.loadtxt( file_x)

draws = []
others = []

for i in xrange(25000):
	if( data_x[i] == 1.0):
		draws.append( match_quality[i])
	else:
		others.append( match_quality[i])

draws = np.array( draws)
others = np.array( others)

print draws
#gaussian_numbers = normal(size=1000)
#uniform_numbers = uniform(low=-3, high=3, size=1000)
plt.hist(draws, bins=50, histtype='stepfilled', color='r', label='Draws')
plt.hist(others, bins=50, histtype='stepfilled', color='b', alpha=0.5, label='Win/Lose')
plt.ylim([0,1000])
plt.title("Draw Win/Lose Distribution")
plt.xlabel("Match Quality (A+B)")
plt.ylabel("Frequency")
plt.legend()
plt.show()