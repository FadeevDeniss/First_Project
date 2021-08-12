import requests as rq
from bs4 import BeautifulSoup

print('Введите запрос: ')
request = input()
r = rq.get(
    'https://www.avito.ru/yaroslavl',
    params={'q': request}
)
soup = BeautifulSoup(r.text, 'html.parser')
for tag in soup.find_all(attrs={'itemprop': 'price'}, limit=5):
    print(str(tag).split('"')[1], "RUB")



