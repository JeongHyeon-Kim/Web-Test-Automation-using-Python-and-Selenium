from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# WebDriver Chrome browser 가져오기
driver = webdriver.Chrome()

# 브라우저 구동
url = "http://www.naver.com/"
driver.get(url)

elem = driver.find_element_by_name("query")
elem.send_keys("python")
elem.send_keys(Keys.RETURN) # Enter 키 입력
