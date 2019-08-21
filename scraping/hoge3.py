import requests
from bs4 import BeautifulSoup

url = 'https://gamewith.jp/shironeko/article/show/161912'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

with open('test.txt', mode='w', encoding='utf-8') as fw:
    fw.write(soup.find("div", "chara_table").text)
