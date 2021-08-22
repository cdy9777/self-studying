from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://beta-flight.naver.com/')

# 날짜 선택
browser.find_element_by_xpath(
    '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(2)

browser.find_element_by_xpath(
    '//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[6]/button/b').click()

browser.find_element_by_xpath(
    '//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/button/b').click()

# 갈 곳 선택
browser.find_element_by_xpath(
    '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/b').click()

browser.find_element_by_xpath(
    '//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/section/button[1]').click()
browser.find_element_by_xpath(
    '//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/section/div/button[2]/i[1]').click()

# 검색
browser.find_element_by_xpath(
    '//*[@id="__next"]/div/div[1]/div[4]/div/div/button/span').click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div[2]/div[2]/div')))
    print(elem.text)

finally:
    browser.quit()
