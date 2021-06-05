import time
from selenium import webdriver

# Chrome
#driver = webdriver.Chrome(r"C:\Users\CHAMP03\edu\chromedriver.exe")
driver = webdriver.Chrome()

# Firefox
#driver = webdriver.Firefox() # 같은 경로에 geckodriver.exe 파일 두기

driver.get("http://www.naver.com/")
time.sleep(2) # 2초 동안 대기
driver.close()
