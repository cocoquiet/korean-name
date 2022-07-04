import requests
import urllib3
from bs4 import BeautifulSoup
import json
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print('reset file')
with open('nameList.txt', 'w', encoding='euc-kr') as f:
    f.write('')

for page in range(1, 31):
    url = f'https://api.namechart.kr/chart/overall?gender=t&page={page}&size=100'

    try:
        response = requests.get(url, verify=False)
    except:
        print('error: restart')
        time.sleep(2)
        response = requests.get(url, verify=False)

    if response.status_code == 200:
        print('page %2d start'%page)
        
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        with open('nameList.txt', 'a', encoding='euc-kr') as f:
            for item in json.loads(soup.text)['items']:
                name = item['name']
                f.write(f'{name}\n')

    else : 
        print(response.status_code)
        break