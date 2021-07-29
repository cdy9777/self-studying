import re
import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
for i in range(1, 6):
    url = 'https://www.coupang.com/np/search?rocketAll=false&q=%EB%85%B8%ED%8A%B8%EB%B6%81&brand=&offerCondition=&filter=&availableDeliveryFilter=&filterType=&isPriceRange=false&priceRange=&minPrice=&maxPrice=&page={}&trcid=&traid=&filterSetByUser=true&channel=user&backgroundColor=&component=&rating=0&sorter=scoreDesc&listSize=36'.format(
        i)
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')
    notebooks = soup.find_all(
        'li', attrs={'class': re.compile('^search-product')})
    for notebook in notebooks:
        if notebook.find('span', attrs={'class': 'ad-badge-text'}):
            continue

        notebook_name = notebook.find(
            'div', attrs={'class': 'name'}).get_text()
        notebook_price = notebook.find(
            'strong', attrs={'class': 'price-value'}).get_text()
        if notebook.find('em', attrs={'class': 'rating'}):
            notebook_score = notebook.find(
                'em', attrs={'class': 'rating'}).get_text()
        else:
            # print('평점 없음')
            continue
        if notebook.find('span', attrs={'class': 'rating-total-count'}):
            notebook_people = notebook.find(
                'span', attrs={'class': 'rating-total-count'}).get_text()
        else:
            # print('평점 수 없음')
            continue
        if float(notebook_score) > 4.5 and int(notebook_people[1:-1]) > 70:
            print(notebook_name, notebook_price,
                  notebook_score, notebook_people)


# notebook = soup.find('li', attrs={'class': re.compile('^search-product')})
# print(notebook)
# notebook_name = notebook.find('div', attrs={'class': 'name'})
# print(notebook_name.get_text())
