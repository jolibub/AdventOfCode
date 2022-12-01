#Import Input
with open('./Puzzel1Input.txt') as f:
  lines = f.readlines()
inputData = []
for l in lines:
  inputData.append(l.strip('\n'))

#Puzzel Solution 1
caloriesPerElv = []
temp = 0
for n in inputData:
  if n != '':
    temp += int(n)
  else:
    caloriesPerElv.append(temp)
    temp = 0
print(max(caloriesPerElv))

#Puzzel Solution 2
print(sum(sorted(caloriesPerElv, reverse=True)[:3]))