import requests
from bs4 import BeautifulSoup


#base_url = 'https://hh.ru/'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
#params = {'text' : 'Data-инженер', 'area' : 1, 'currency_code' : 'RUR', 'experience' : 'doesNotMatter', 'order_by' : 'relevance', 'search_period' : 0, 'items_on_page' : 20, 'no_magic' : 'true', 'L_save_area' : 'true'}
    #'text' : 'Data-инженер', 'area' : 1, 'fromSearchLine' : 'false', 'items_on_page' : 20
#url = f'{base_url}/search/vacancy?'
url = 'https://hh.ru/search/vacancy?text=Data-%D0%B8%D0%BD%D0%B6%D0%B5%D0%BD%D0%B5%D1%80&area=1&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=20&no_magic=true&L_save_area=true'

response = requests.get(url, headers=headers)
print(response)
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