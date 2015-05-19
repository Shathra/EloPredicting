def to_int( list):

	for i in xrange( len(list)):
		list[i] = int(list[i])

def get_mistakes( list):

	white = 0
	black = 0

	score = 0
	for i in xrange(len(list)):
		if i % 2 == 0:
			if list[i] < score - 300:
				white += 1
		else:
			if list[i] > score + 300:
				black += 1
		score = list[i]

	result = [None] * 3
	result[0] = white
	result[1] = black
	result[2] = white+black

	return result

path = "../data/stockfish_norm.csv"

games = open( path)

scores = [None] * 50000
for i,row in enumerate(games):
	splitted = row.split( ",")[1]
	if len(splitted) < 3:
		scores[i] = 0
		continue
	scores[i] = splitted.split( " ")
	to_int( scores[i])

'''
mean = open( "results/mean.fea", "w")
for i, agame in enumerate(scores):
	if( type(agame) is list):
		mean.write( str(sum(agame) / float(len(agame))) + "\n")
	else:
		mean.write( str(agame) + "\n")
mean.close()
'''

mistakes = open( "results/no_of_mistakes", "w")
mistakes_scaled = open( "results/no_of_mistakes_scaled", "w")
wmistakes = open( "results/no_of_white_mistakes", "w")
wmistakes_scaled = open( "results/no_of_white_mistakes_scaled", "w")
bmistakes = open( "results/no_of_black_mistakes", "w")
bmistakes_scaled = open( "results/no_of_black_mistakes_scaled", "w")

for agame in scores:
	if( type(agame) is int):
		mistakes.write( "0\n")
		mistakes_scaled.write( "0\n")
		wmistakes.write( "0\n")
		wmistakes_scaled.write( "0\n")
		bmistakes.write( "0\n")
		bmistakes_scaled.write( "0\n")
	else:
		result = get_mistakes( agame)
		mistakes.write( str( result[2]) + "\n")
		mistakes_scaled.write( str( result[2] / float( len(agame))) + "\n")
		wmistakes.write( str( result[0]) + "\n")
		wmistakes_scaled.write( str( result[0] / float( len(agame))) + "\n")
		bmistakes.write( str( result[1]) + "\n")
		bmistakes_scaled.write( str( result[1] / float( len(agame))) + "\n")

mistakes.close()
mistakes_scaled.close()
wmistakes.close()
wmistakes_scaled.close()
bmistakes.close()
bmistakes_scaled.close()

games.close()