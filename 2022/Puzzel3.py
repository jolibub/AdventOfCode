import ImportPuzzelData as ipd

#Import Input
lines = ipd.get(2022, 3)

inputData = lines.split('\n')
inputData.pop(-1)

#Puzzel Solution 1

items = []

for l in inputData:
	middle = int(len(l) / 2)
	for f in l[:middle]:
		if l[middle:].find(f) >= 0:
			items.append(f)
			break

print(sum(list(map('@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.find, items)))) # @ in front to increase index by one

#Puzzel Solution 2

badges = []
for g in range(0, len(inputData), 3):
	for b in inputData[g]:
		if inputData[g+1].find(b) >= 0:
			if inputData[g+2].find(b) >= 0:
				badges.append(b)
				break

print(sum(list(map('@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.find, badges))))