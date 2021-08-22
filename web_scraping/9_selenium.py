from selenium import webdriver
import time


browser = webdriver.Chrome('./chromedriver.exe')  # 같은 폴더에 있으면 괄호 안 내용 생략 가능
browser.get('http://www.naver.com')

# 네이버 로그인
browser.find_element_by_class_name('link_login').click()

# ID/PW 입력
browser.find_element_by_id('id').send_keys('naverlogin')
browser.find_element_by_id('pw').send_keys('naverpw')
browser.find_element_by_id('log.login').click()

time.sleep(3)

# ID/PW 재입력
browser.find_element_by_id('id').clear()
browser.find_element_by_id('id').send_keys('naverid')

# html 문서가져오기
print(browser.page_source)
browser.close()  # 현재 탭만 종료 browser.quit()은 전체 종료.
