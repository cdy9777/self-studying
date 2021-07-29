import requests
from bs4 import BeautifulSoup


for year in range(2016, 2021):
    url = 'https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'.format(
        year)
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')

    images = soup.find_all('img', attrs={'class': 'thumb_img'})
    for index, image in enumerate(images):
        image_url = image['src']
        if image_url.startswith('//'):
            image_url = 'https:'+image_url

        movie_img = requests.get(image_url)
        movie_img.raise_for_status()
        with open('image_{}_{}.jpg'.format(year, index+1), 'wb') as f:
            f.write(movie_img.content)

        if index >= 4:
            break
