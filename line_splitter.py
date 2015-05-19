import sys

base = str(sys.argv[1])
target = str(sys.argv[2])
start = int(sys.argv[3])
n = int(sys.argv[4])

read = open( base)
write = open( target, "w")

for i, line in enumerate( read):
	if i >= start and i < start + n:
		write.write( line)

read.close()
write.close()