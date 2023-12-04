import ImportPuzzelData as ipd
import re

#Import Input
lines = ipd.get(2023, 1, True).split('\n')
inputData = []
for l in lines:
  inputData.append(l.strip('\n'))

#Puzzel Solution 1
calibrationSum = 0

for n in inputData:
  numberFirst = re.search(r"\d", n)
  numberLast = re.search(r"\d(?!.*\d)", n)
  if numberFirst != None:
    calibrationSum += int(numberFirst.group()) * 10 + int(numberLast.group())
print(calibrationSum)

#Puzzel Solution 2
