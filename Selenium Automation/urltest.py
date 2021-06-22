from selenium import webdriver
import time
import ddt # pip install ddt

driver = webdriver.Chrome("chromedriver.exe")

f = open("url.txt", "r")

url = f.readlines()

for i in range(0, 3):
    real_url = url[i]
    driver.get(real_url)
    time.sleep(1)
f.close()
driver.close()
