import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

rank_01 = soup.find('li', attrs={'class': 'rank01'})
rank_02 = rank_01.find_next_siblings('li')
# print(rank_01.a.get_text())
# print(rank_02.a.get_text())
# print(rank_02.find_previous_sibling().a.get_text())
rank_list = list()
rank_list.append(rank_01)
rank_list += rank_02
for rank in rank_list:
    print(rank.a.get_text())
