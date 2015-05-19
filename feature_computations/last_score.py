path = "../data/stockfish_norm.csv"

scores = open( path)
last_scores = open( "last_scores.fea", "w")
for row in scores:
	last_scores.write( row.rsplit(" ", 1)[1])

scores.close()
last_scores.close()