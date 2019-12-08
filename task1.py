# 1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json.
import json

import requests

url = 'https://api.github.com/users/deim76/repos'
header = ''

def save_file(data:list):
    with open('repos.json', 'w') as file:
        for item in data:
            file.write(json.dumps(item))
params=[]
request_url = requests.get(url)
data = request_url.json()
params.append(data)
while request_url.next:
    request_url = requests.get(request_url.next)
    params.append(request_url.json())
print(1)

