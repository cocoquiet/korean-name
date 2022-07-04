import requests
import json
from bs4 import BeautifulSoup
import time


session = requests.Session()

for page in range(1, 36):
    url = f'http://api.namechart.kr/chart/overall?gender=t&page={page}&size=100'

    try:
        response = session.get(url, verify=False)
    except:
        print('에러: 2초 딜레이')
        time.sleep(2)
        response = session.get(url, verify=False)

    if response.status_code == 200:
        print(f'page {page} start')
        
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        with open('nameList', 'a', encoding='euc-kr') as f:
            for item in json.loads(soup.text)['items']:
                name = item['name']
                f.write(f'{name}\n')

        print(f'page {page} end')

    else : 
        print(response.status_code)
        break