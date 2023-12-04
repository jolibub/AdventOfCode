import requests
import json
import os

# os.environ['REQUESTS_CA_BUNDLE'] = 

with open('./secret.json') as f:
  j = json.load(f)
  
proxies = {
  'http':f'http://{j["proxyUser"]}:{j["proxyPass"]}@172.21.255.254:8080',
  'https':f'http://{j["proxyUser"]}:{j["proxyPass"]}@172.21.255.254:8080'
}

def get(year: int, day: int, useProxy: bool):
  cookies = dict(session=j['session'])
  res = ''
  if useProxy:
    print('proxy')
    res = requests.get(f'https://adventofcode.com/{str(year)}/day/{str(day)}/input', proxies=proxies, cookies=cookies, verify=False)
  else:
    res = requests.get(f'https://adventofcode.com/{str(year)}/day/{str(day)}/input', cookies=cookies)
  inputData = res.text

  return inputData