'''
path = "../data/data.pgn"

games = open( path)
result = open( "chechmate_move_done.fea", "w")

no = 0
new = False
value = "0"
for row in games:
	if row[0] == '[':
		new = True
	else:
		if new:
			result.write( value + "\n")
			value = "0"

		new = False
		if row.find( "#") != -1:
			value = "1"

games.close()
result.close()
'''

cmd = [None] * 50000
win = [None] * 50000
fp = open("chechmate_move_done.fea")
for i, row in enumerate(fp):
	cmd[i] = row
fp.close()

fp = open("results/winner.fea")
for j, row in enumerate(fp):
	win[j] = row
fp.close()

print win

fp = open("results/chechmate_move_done2.fea", "w")
for i in xrange( 50000):
	if win[i] == "0\n":
		fp.write( "-1\n")
	else:
		if cmd[i] == "1\n":
			fp.write( "1\n")
		else:
			fp.write( "0\n")
fp.close()