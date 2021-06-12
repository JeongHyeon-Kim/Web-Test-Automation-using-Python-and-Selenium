# G마켓 로그인하기
from selenium import webdriver

# WebDriver Chrome browser 가져오기
driver = webdriver.Chrome()

# 브라우저 구동
url = "http://www.gmarket.co.kr/"
driver.get(url)

# 로그인 정보 입력
id = "{id}"
pw = "{pwd}"
xpaths = {'id': "//input[@name='id']", 'pw': "//input[@name='pwd']"}

# < 로그인하기 >
# 1. 로그인 창 열기
driver.find_element_by_class_name('link__usermenu').click()

# 2. 로그인 정보 넣기
driver.find_element_by_xpath(xpaths['id']).send_keys(id)
driver.find_element_by_xpath(xpaths['pw']).send_keys(pw)

# 3. 로그인 버튼 클릭
driver.find_element_by_class_name('button_login').click()
