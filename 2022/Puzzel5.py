import ImportPuzzelData as ipd

#Import Input
lines = ipd.get(2022, 5)

inputData = lines.split('\n')
inputData.pop(-1)

#Functions
def execMove(state: list, move: str):
	moveSplit = move.split()
	amount, moveFrom, moveTo = int(moveSplit[1]), int(moveSplit[3]) - 1, int(moveSplit[5]) - 1

	for i in range(0,amount):
		state[moveTo].append(state[moveFrom][-1])
		state[moveFrom].pop()

def execMoveStack(state: list, move: str):
	moveSplit = move.split()
	amount, moveFrom, moveTo = int(moveSplit[1]), int(moveSplit[3]) - 1, int(moveSplit[5]) - 1

	print(state[moveFrom][- amount:])

	state[moveTo].extend(state[moveFrom][- amount:])
	del state[moveFrom][- amount:]

#Puzzel Solution 1

inputState = []
state = []
moves = []

for n, l in enumerate(inputData):
	if l == '':
		inputState = inputData[:n]
		moves = inputData[n + 1:]


for a in range(0, int(inputState[-1].split()[-1])):
	state.append([])

inputState.pop()
inputState.reverse()

for b in inputState:
	b = b.replace('    ', ' [-] ')
	b = b.split()
	for i, z in enumerate(b):
		state[i].append(z)

for q, t in enumerate(state):
	while '[-]' in state[q]:
		state[q].remove('[-]')

stateP1 = state.copy()

#Execute Moves
for m in moves:
	execMove(stateP1, m)

outputP1 = []
for g in stateP1:
	outputP1.append(g[-1].replace('[', '').replace(']', ''))

print(''.join(outputP1))


#Puzzle Solution 2

stateP2 = state.copy()

#Execute Moves
for m in moves:
	execMoveStack(stateP2, m)

outputP2 = []
for g in stateP2:
	outputP2.append(g[-1].replace('[', '').replace(']', ''))

print(''.join(outputP2))