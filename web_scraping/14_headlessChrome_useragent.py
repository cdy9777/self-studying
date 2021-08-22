from selenium import webdriver


options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('window-size=1920x1080')
options.add_argument(
    'user-agent=유저에이전트')

url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'

browser = webdriver.Chrome(options=options)
browser.maximize_window()
browser.get(url)

detected_value = browser.find_element_by_id('detected_value')
print(detected_value.text)
