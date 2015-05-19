import numpy as np

def parseData( path, n=50000, startWith=0):

    games = open( path)

    whiteWins = np.zeros( shape=(n, 1))
    blackWins = np.zeros( shape=(n, 1))
    draws = np.zeros( shape=(n, 1))
    whiteElo = np.zeros( shape=(n, 1))
    blackElo = np.zeros( shape=(n, 1))

    i = -1
    for row in games:
        if i == n:
            break
        if row.startswith('[Event'):
            i += 1
        elif row.startswith('[Result'):
            result = row.split('"')[1]
            if result == '1/2-1/2':
                draws[i] = 1.0
            elif result == '1-0':
                whiteWins[i] = 1.0
            else:
                blackWins[i] = 1.0
        elif row.startswith('[WhiteElo'):
            whiteElo[i] = int(row.split('"')[1])
        elif row.startswith('[BlackElo'):
            blackElo[i] = int(row.split('"')[1])

    results = { "whiteWins":whiteWins,
                "blackWins":blackWins,
                "draws":draws,
                "whiteElo":whiteElo,
                "blackElo":blackElo}

    return results
