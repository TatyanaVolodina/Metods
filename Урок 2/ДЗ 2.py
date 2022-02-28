import requests
from bs4 import BeautifulSoup


base_url = 'https://hh.ru/'
headers = {'User Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
params = {'text' : 'Data-инженер', 'area' : 1, 'fromSearchLine' : 'false'}
url = f'{base_url} /search/vacancy?'

response = requests.get(url, headers=headers, params=params)
dom = BeautifulSoup(response.text, 'html.parser')

vacancys = dom.find_all('div', {'class' : 'vacancy-serp-item vacancy-serp-item_redesigned'})

vacancys_list = []

for vacancy in vacancys:
    vacancy_1 = {}
    vac = vacancy.find('a', {'class' : 'bloko-link'})
    name = vac.text
    link = base_url + vac['href']
    sale = vacancy.find('span', {'data-qa', 'vacancy-serp__vacancy-compensation'})
    price = sale.text
    vacancy_1['name'] = name
    vacancy_1['link'] = link
    vacancy_1['price'] = price
    vacancys_list.append(vacancy_1)
 
print(vacancys_list)
#print(vacancys)