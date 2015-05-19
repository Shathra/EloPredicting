import numpy as np

path = "data/stockfish.csv"
result_path = "data/stockfish_norm.csv"
scores = open(path)
fd = open( result_path, "w")
i = 0;

for row in scores:
	index = 0
	found = row.find( "NA", index)
	while( found != -1):
		space = row[:found - 1].rfind( " ")
		last_score = row[space + 1: found - 1]
		row = row.replace( "NA", last_score, 1)
		found = row.find( "NA", index)
		i += 1;
	fd.write( row)

print i
scores.close()
fd.close()
