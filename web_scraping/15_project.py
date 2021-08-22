import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': '유저 에이전트'}


def weather_today():
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_sug.asiw&fbm=1&acr=1&acq=%EC%84%9C%EC%9A%B8+&qdt=0&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8'
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')

    today_weather = soup.find('p', attrs={'class': 'cast_txt'}).get_text()
    temperature = soup.find('span', attrs={'class': 'todaytemp'}).get_text()
    # temperature = soup.find('p', attrs = {'class' : 'info_temperature'}).get_text().replace('도씨','')
    lowest_temp = soup.find('span', attrs={'class': 'min'}).get_text()
    highest_temp = soup.find('span', attrs={'class': 'max'}).get_text()
    morning_rate = soup.find('li', attrs={'class': 'date_info today'}).find_all(
        'span', attrs={'class': 'rain_rate'})[0].find('span', attrs={'class': 'num'}).get_text()
    evening_rate = soup.find('li', attrs={'class': 'date_info today'}).find_all(
        'span', attrs={'class': 'rain_rate'})[1].find('span', attrs={'class': 'num'}).get_text()
    pm_10 = soup.find_all('dd', attrs={'class': 'lv2'})[0].get_text()
    pm_25 = soup.find_all('dd', attrs={'class': 'lv2'})[1].get_text()

    print('[오늘의 날씨]')
    print(f'[{today_weather}]')
    print(f'현재 {temperature}도 (최저 {lowest_temp} / 최고 {highest_temp})')
    print(f'오전 강수확률 {morning_rate}%/오후 강수확률 {evening_rate}%\n')
    print(f'미세먼지 {pm_10}')
    print(f'초미세먼지 {pm_25}\n')


def header_news():
    url = 'https://news.naver.com/'

    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')

    news = soup.find('ul', attrs={'class': 'hdline_article_list'}).find_all(
        'li', limit=3)
    print('[헤드라인 뉴스]')

    for idx, new in enumerate(news):
        new_headline = new.div.a.get_text().strip()
        new_link = new.a['href']

        print(f'{idx+1}. {new_headline}')
        print('(링크 : https://news.naver.com/' + new_link + ')\n')

    print()


def it_news():
    url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230'

    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')

    news = soup.find('ul', attrs={'class': 'type06_headline'}).find_all('li')

    print('[IT/일반 뉴스]')

    for idx, new in enumerate(news):
        new_headline = new.dt.find_next_sibling().get_text().strip()
        new_link = new.a['href']

        print(f'{idx+1}. {new_headline}')
        print('(링크 : ' + new_link + ')\n')

        if idx >= 2:
            break

    print()


def today_english():
    url = 'https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english'

    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')
    text = soup.find_all('div', attrs={'class': 'conv_in'})
    en_texts = text[1].find_all('span', 'conv_sub')
    kor_texts = text[0].find_all('span', 'conv_sub')

    print('[오늘의 영어 회화]')
    print('(영어 지문)')
    for text in en_texts:
        print(text.get_text())
    print()
    print('(한글 지문)')
    for text in kor_texts:
        print(text.get_text())


if __name__ == "__main__":
    weather_today()
    header_news()
    it_news()
    today_english()
