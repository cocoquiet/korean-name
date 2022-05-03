import requests
from bs4 import BeautifulSoup


# for page in range(1, 36):
    # url = f'http://api.namechart.kr/chart/overall?gender=t&page={page}&size=100'

url = 'https://api.namechart.kr/chart/overall?gender=t&page=1&size=100'


response = requests.get(url, verify=False)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    f = open('nameDB.json')
    f.write(soup)

else : 
    print(response.status_code)