import requests
from lxml import html
from pprint import pprint
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
response = requests.get('https://lenta.ru/', headers=headers)
dom = html.fromstring(response.text)
items = dom.xpath("//a[contains(@class, 'card-mini _topnews')]")
item_list = []
for item in items:
    item_info = {}
    name = item.xpath(".//span[contains(@class, 'card-mini__title')]/text()")
    link = item.xpath(".//div[@class='card-mini__text']/../@href")
    date_time = item.xpath(".//div[@class='card-mini__text']/div/time/text()")

    item_info['name'] = name
    item_info['link'] = link
    item_info['date_time'] = date_time

    item_list.append(item_info)

def load_data_to_mongodb(data, name):
    client = MongoClient('127.0.0.1', 27017)
    db = client['lenta.ru']

    items = db.items
    not_added_data = []
    duplicate_data = []
    for one in data:
        try:
            items.insert_one(one)
        except DuplicateKeyError:
            duplicate_data.append(one)
        except:
            not_added_data.append(one)

pprint(item_list)

