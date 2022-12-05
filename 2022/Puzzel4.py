# TODO use import for puzzel input

f = open("puzzelinput4.txt", "r")

lines = f.read()
inputData = lines.split('\n')

#Puzzel Solution 1

splitlist = list(map(lambda x: x.split(','), inputData))

fullsplit = list(map(lambda x: list(map(lambda y: y.split('-'), x)) ,splitlist))

nrOfPairs = 0

for r in fullsplit:
	if (int(r[0][0]) in range(int(r[1][0]), int(r[1][1]) + 1) and int(r[0][1]) in range(int(r[1][0]), int(r[1][1]) + 1)) or (int(r[1][0]) in range(int(r[0][0]), int(r[0][1]) + 1) and int(r[1][1]) in range(int(r[0][0]), int(r[0][1]) + 1)):
		nrOfPairs += 1

print(nrOfPairs)

#Puzzel Solution 2
nrOfPairsOverlapping = 0

for r in fullsplit:
	if int(r[0][0]) in range(int(r[1][0]), int(r[1][1]) + 1) or int(r[0][1]) in range(int(r[1][0]), int(r[1][1]) + 1) or int(r[1][0]) in range(int(r[0][0]), int(r[0][1]) + 1) or int(r[1][1]) in range(int(r[0][0]), int(r[0][1]) + 1):
		nrOfPairsOverlapping += 1

print(nrOfPairsOverlapping)