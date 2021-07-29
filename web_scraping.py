import requests
from bs4 import BeautifulSoup as bs
headers = {
    'authority': 'api.kurly.com',
    'sec-ch-ua': '^\\^',
    'accept': 'application/json, text/plain, */*, application/json',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjYXJ0X2lkIjoiYzA1ZjU0ZDgtZjdkMC00YTFlLTk5YWQtNzFjOGVhM2QzMTM3IiwiaXNfZ3Vlc3QiOnRydWUsInV1aWQiOm51bGwsIm1fbm8iOm51bGwsIm1faWQiOm51bGwsImxldmVsIjpudWxsLCJzdWIiOm51bGwsImlzcyI6Imh0dHA6Ly9ta3dlYi5hcGkua3VybHkuc2VydmljZXMvdjMvYXV0aC9ndWVzdCIsImlhdCI6MTYyNjQ3OTE5OSwiZXhwIjoxNjI2NDgyNzk5LCJuYmYiOjE2MjY0NzkxOTksImp0aSI6IlBJOG8yWVptNUc0ZnhxbFUifQ.E7eeHBgejwzjAnhMjPkSZR3p_ByZVIcbwX4wzZd6iHo',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://api.kurly.com/xdomain?ver=1',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': '_fbp=fb.1.1625723538957.844333799; __cfruid=f3b364be8d04961ace18636f957a0e083f261524-1626479199; _gid=GA1.2.1135680672.1626479200; _gat=1; cookie_check=0; XSRF-TOKEN=eyJpdiI6ImQyQ2FZTmc5MWwzQ2laaHVhU0dVWWc9PSIsInZhbHVlIjoibWVtdGRUNEx2R25JWUJhUjZ0am9xNDFDbzFUM2IrUHdacmZmbEtpbnhCTTE5bHlXZzJvcXZpWXorUEVUREtQSCIsIm1hYyI6ImIwY2MyZTJhZTBmMWE1NGFlN2Y2YzdiODEyYzcwMjY0Mjk5NzMwZWJkOTVjZWM1ODBkZDA4NTFlZjkzMGU4NWMifQ^%^3D^%^3D; api_kurly_com_session=eyJpdiI6IkpWc2lhRW9weVpMMU9LK1VmRmlmU1E9PSIsInZhbHVlIjoiYXFwOEJ6QXAzK1ZRWUtEKzJvT2pEY1U0WnY3MHdkeCtUbzFxUkZXVDRzXC9na0tiMzllZGhMOXVWNTJxYXRFZUEiLCJtYWMiOiI1ZTdhYThhZmIxMzM5Y2Q2ZGI2MzVhNWI5YTdiYzM1ODExY2E3ZGQ5NTZmMTBhYTMzOTVhMGFhMmYxN2RhYWQ3In0^%^3D; amplitude_id_65bebb55595beb82e78d5d1ae808702ckurly.com=eyJkZXZpY2VJZCI6IjE3Y2UwYWMyLWNiNGItNDkzNi1iMjk4LWY0Mjg0MzUyMWY0MFIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTYyNjQ3OTIwMDQ5MywibGFzdEV2ZW50VGltZSI6MTYyNjQ3OTI0MzMxOCwiZXZlbnRJZCI6MCwiaWRlbnRpZnlJZCI6Miwic2VxdWVuY2VOdW1iZXIiOjJ9; _ga_2K2GN0FFY0=GS1.1.1626479200.2.1.1626479243.17; _ga=GA1.1.855695046.1625723538',
}

params = (
    ('page_limit', '99'),
    ('page_no', '1'),
    ('delivery_type', '0'),
    ('sort_type', ''),
    ('ver', '1626479243928'),
)

response = requests.get(
    'https://api.kurly.com/v1/home/newproducts', headers=headers, params=params)
soup = bs(response.text, "html.parser")
print(soup)
items = soup.select(".inner_listgoods .list .item")
print(items)
# for item in items:
#     item_name = item.select_one('a > span.name')
#     print(item_name.text)
# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://api.kurly.com/v1/home/newproducts?page_limit=99&page_no=1&delivery_type=0&sort_type=&ver=1626479243928', headers=headers)


# import requests
# from bs4 import BeautifulSoup as bs


# url = 'https://www.10000recipe.com/recipe/list.html?q=%EB%B0%80%ED%91%80%EC%9C%A0%EB%82%98%EB%B2%A0'
# response = requests.get(url)
# response.raise_for_status()

# soup = bs(response.text, 'html.parser')

# rc_list = soup.select('#contents_area_full > ul > ul > li')
# # print(rc_list)
# rc_name_list = []
# for rc in rc_list:
#     rc_name = rc.select_one(
#         'div.common_sp_caption > div.common_sp_caption_tit.line2')
#     rc_name_list.append(rc_name.text)

# print(rc_name_list)


# rc_name_list = [rc.select_one(
#     '.common_sp_caption > .common_sp_caption_tit line2').text for rc in rc_list]


# url = 'https://comic.naver.com/webtoon/detail?titleId=703852&no=153&weekday=tue'
# response = requests.get(url)

# soup = bs(response.text, 'html.parser')

# cut_list = soup.select('#comic_view_area > div.wt_viewer> img')

# image_src_list = []
# for cut in cut_list:
#     img = cut.get('src')
#     image_src_list.append(img)
# # image_src_list = [cut.get('src') for cut in cut_list]
# ipyplot.plot_images(image_src_list, img_width=800)


# url = 'https://comic.naver.com/webtoon/weekdayList?week=tue'
# response = requests.get(url)

# soup = bs(response.text, 'html.parser')
# scraps = soup.select(
#     '#content > div.list_area.daily_img > ul > li')

# for scrap in scraps:
#     print('웹툰제목 :', scrap.select_one('dt > a').text)
#     print('작가 :', scrap.select_one('.desc > a').text)
#     print('평점 : ', scrap.select_one('dd > .rating_type > strong').text)
#     print()
