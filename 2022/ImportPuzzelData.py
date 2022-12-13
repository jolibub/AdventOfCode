import requests
import json

with open('./secret.json') as f:
  j = json.load(f)
print(j['session'])
  
proxies = {
  'http':'http://172.21.255.254:8080',
  'https':'http://172.21.255.254:8090'
}

def get(year: int, day: int, useProxy: bool):
  cookies = dict(session=j['session'])
  res = ''
  if useProxy:
    res = requests.get(f'https://adventofcode.com/{str(year)}/day/{str(day)}/input', cookies=cookies, auth=(j['proxyUser'], j['proxyPass']), proxies=proxies)
  else:
    res = requests.get(f'https://adventofcode.com/{str(year)}/day/{str(day)}/input', cookies=cookies)
  inputData = res.text

  return inputData