'''
def find( element, list):

	for i, j in enumerate( list):

		if( j == element):
			return i;

	return -1

data_path = "../data/data_uci.pgn"

fd = open( data_path)
'''

def find( element, list):

	for i, j in enumerate( list):

		if( j[0:2] == element):
			return i;

	return -1

data_path = "../data/data_uci.pgn"

fd = open( data_path)

'''
fd_white = open( "results/castle_white.fea", "w")
fd_black = open( "results/castle_black.fea", "w")
fd_castle = open( "results/castle.fea", "w")

for row in fd:

	if row[0] != '\n' and row[0] != '[':
		moves = row.split( ' ')
		white_c = find( "e1g1", moves)
		black_c = find( "e8g8", moves)

		if( white_c == -1):
			white_c = find( "e1c1", moves)

		if( white_c == -1):
			w = 1

		else:
			w = white_c / float( len(moves))

		if( black_c == -1):
			black_c = find( "e8c8", moves)

		if( black_c == -1):
			b = 1

		else:
			b = white_c / float( len(moves))
		
		fd_white.write( str( w) + "\n")
		fd_black.write( str( b) + "\n")
		fd_castle.write( str( (w+b) * 0.5) + "\n")

fd.close()
fd_white.close()
fd_castle.close()
fd_black.close()
'''

#Queen First Move

fd_white = open( "results/queen_white.fea", "w")
fd_black = open( "results/queen_black.fea", "w")
fd_queen = open( "results/queen.fea", "w")

for row in fd:

	if row[0] != '\n' and row[0] != '[':
		moves = row.split( ' ')
		white_c = find( "d1", moves)
		black_c = find( "d8", moves)

		#if( white_c == -1):
		#	white_c = find( "e1c1", moves)

		if( white_c == -1):
			w = 1

		else:
			w = white_c / float( len(moves))

		#if( black_c == -1):
		#	black_c = find( "e8c8", moves)

		if( black_c == -1):
			b = 1

		else:
			b = white_c / float( len(moves))
		
		fd_white.write( str( w) + "\n")
		fd_black.write( str( b) + "\n")
		fd_queen.write( str( (w+b) * 0.5) + "\n")

fd.close()
fd_white.close()
fd_queen.close()
fd_black.close()