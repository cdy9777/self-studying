import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': '유저-에이전트',
    'Accept-Language': 'ko-KR,ko'}
url = 'https://play.google.com/store/movies/top'
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

# with open('movie.html',  'w', encoding='utf-8') as f:
#     f.write(soup.prettify())

movies = soup.find_all('div', attrs={'class': 'ImZGtf mpg5gc'})

for movie in movies:
    title = movie.find('div', attrs={'class': 'WsMG1c nnK0zc'}).get_text()
    print(title)
