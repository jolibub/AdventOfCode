import ImportPuzzelData as ipd

#Import Input
lines = ipd.get(2022, 2)

inputData = lines.split('\n')
inputData.pop(-1)

#Puzzel Solution 1          r p s
rpsme = ['X', 'Y', 'Z'] #   1 2 3
rpsyou = ['A', 'B', 'C'] #  1 2 3
res1 = 0

for p in inputData:
  #Add Value for choosen symbol
  res1 += rpsme.index(p[2]) + 1

  #Add Value for game result
  diff = (rpsme.index(p[2]) + 1) - (rpsyou.index(p[0]) + 1)
  if diff == 0: #Draw
    res1 += 3
  elif diff == -1 or diff == 2: #Loose
    res1 += 0
  elif diff == 1 or diff == -2: #Win
    res1 += 6
print(res1)

#Puzzel Solution 2
res2 = 0
gameResult = {'X': 0, 'Y': 3, 'Z': 6}
looseSymbolValue = {'A': 3, 'B': 1, 'C': 2}
winSymbolValue = {'A': 2, 'B': 3, 'C': 1}

for p in inputData:
  res2 += gameResult[p[2]]
  if p[2] == 'Y':
    res2 += rpsyou.index(p[0]) + 1
  elif p[2] == 'X':
    res2 += looseSymbolValue[p[0]]
  elif p[2] == 'Z':
    res2 += winSymbolValue[p[0]]
print(res2)