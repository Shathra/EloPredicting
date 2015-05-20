fd = open( "last_scores.fea")
fd2 = open( "last_scores2.fea", "w")

for row in fd:
	if row == "\n":
		fd2.write( "0\n")
	else:
		fd2.write( row)

fd.close()
fd2.close()
