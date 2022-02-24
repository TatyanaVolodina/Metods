import requests
from pprint import pprint
import json

url = 'https://api.github.com/users/TatyanaVolodina/repos'
response = requests.get(url)
data = response.json()
list_repos = [repo.get('name') for repo in data]
user_repos = [user.get('full_name') for user in data]

print(type(data))
print(list_repos)
print(user_repos)
