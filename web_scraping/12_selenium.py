from selenium import webdriver
import time
from bs4 import BeautifulSoup

url = 'https://play.google.com/store/movies/top'

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

previous_height = browser.execute_script('return document.body.scrollHeight')

# javascript scroll 제어
while True:
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)

    curr_height = browser.execute_script('return document.body.scrollHeight')

    if curr_height == previous_height:
        break

    previous_height = curr_height

soup = BeautifulSoup(browser.page_source, 'lxml')
movies = soup.find_all('div', attrs={'class': 'Vpfmgd'})

for movie in movies:
    title = movie.find('div', attrs={'class': 'WsMG1c nnK0zc'}).get_text()
    original_price = movie.find('span', attrs={'class': 'SUZt4c djCuy'})

    if original_price:
        original_price = original_price.get_text()
    else:
        continue

    discounted_price = movie.find(
        'span', attrs={'class': 'VfPpfd ZdBevf i5DZme'}).get_text()
    movie_url = movie.find(
        'div', attrs={'class': 'b8cIId ReQCgd Q9MA7b'}).a['href']

    print(f'영화제목 : {title}')
    print(f'할인 전 가격 : {original_price}')
    print(f'할인 후 가격 : {discounted_price}')
    print('영화링크 :' + 'https://play.google.com' + movie_url)
    print('*'*100)
