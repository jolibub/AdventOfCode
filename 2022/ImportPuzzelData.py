import requests

with open('./secret.txt') as f:
  key = f.read()
  
def get(year: int, day: int):
  cookies = dict(session=key)
  res = requests.get(f'https://adventofcode.com/{str(year)}/day/{str(day)}/input', cookies=cookies)
  inputData = res.text

  return inputData