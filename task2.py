# Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
# Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.


import requests
from requests.auth import HTTPBasicAuth
url = 'https://api.github.com/user'
header = '"User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64)'

request_url=requests.get(url, auth=HTTPBasicAuth('deim76', '***'))
request_code = request_url.status_code
with open('log.txt', 'w') as file:
    file.write(f'answer https://api.github.com {request_code}')
