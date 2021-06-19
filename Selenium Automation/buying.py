import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Class 선언
class ShoppingOnInternet():
    def __init__(self):
        self.browser = input("> Which browser do you want? ")

    # WebDriver Chrome browser 가져오기
    def get_browser(self):
        while True:
            if self.browser in ("IE", "ie", "I", "i"):
                self.driver = webdriver.Ie("IEDriverServer.exe")
                break
            elif self.browser in ("Chrome", "chrome", "CH", "ch", "C", "c"):
                self.driver = webdriver.Chrome("chromedriver.exe")
                break
            elif self.browser in ("FireFox", "firefox", "FF", "ff", "F", "f"):
                self.driver = webdriver.Firefox()
                break
            else:
                self.browser = input("Please input the browser again ")
                continue

    # 브라우저 구동
    def invoke_browser(self):
        url = "http://www.gmarket.co.kr/"
        self.driver.get(url)
        self.driver.save_screenshot('1_browser_on.png')
        self.driver.implicitly_wait(1)
        try:
            print('> try - except')
        except "G마켓 - 쇼핑을 다 담다." not in self.driver.title:
            f = open('exceptions.txt', 'rw')
            f.write('Not exect title in drvier.title\n')
            f.close()

    # 로그인하기
    def login_to_homepage(self):
        # 로그인 정보 입력
        id = "{id}"
        pw = "{pwd}"
        xpaths = {'id': "//input[@name='id']", 'pw': "//input[@name='pwd']"}

        # < 로그인하기 >
        # 1. 로그인 창 열기
        self.driver.find_element_by_class_name('link__usermenu').click()

        # 2. 로그인 정보 넣기
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(xpaths['id']).send_keys(id)
        self.driver.find_element_by_xpath(xpaths['pw']).send_keys(pw)
        self.driver.save_screenshot('2_login_screen.png')
        self.driver.implicitly_wait(1)

        # 3. 로그인 버튼 클릭
        self.driver.find_element_by_class_name('button_login').click()

    # 상품 구매하기
    def buy_goods(self):
        # < 책 "대통령의 말하기" 구매하기 >
        # 1.  검색 '대통령의 말하기' -> 버튼 클릭!
        self.driver.find_element_by_name("keyword").clear() # 검색창 clear 후, 검색창에 상품 이름 검색
        self.driver.find_element_by_name("keyword").send_keys(u"대통령의 말하기")
        self.driver.find_element_by_class_name("button__search").click()
        self.driver.save_screenshot('3_search_result.png')
        self.driver.implicitly_wait(3)

        # 2. 검색 결과 중 상품 선택
        self.driver.find_element_by_class_name("text__item").click()

        # 상품 상세 설명 및 구매 창이 열릴 때 새창이 열린다! window를 새창으로 바꿔주지 않으면 element ID를 찾지 못한다!
        for windows in self.driver.window_handles:
            pass
        current_window = windows

        self.driver.switch_to_window(current_window)
        self.driver.implicitly_wait(5)
        self.driver.save_screenshot('4_select_goods.png')

        # 3-1. 구매하기 버튼 클릭
        #self.driver.implicitly_wait(5)
        #self.driver.find_element_by_id("coreInsOrderBtn").click()
        #self.driver.find_element_by_xpath('//*[@id="coreInsOrderBtn"]').click()
        #element = self.driver.find_element_by_xpath('//*[@id="coreInsOrderBtn"]')
        #self.driver.execute_script("arguments[0].click();", element) # 다른 요소로 감싸고 있기 때문에 execute_script로 실행, 참고:
        #self.driver.save_screenshot('5_purchase_goods.png')

        # 3-2. 장바구니 버튼 클릭
        element = self.driver.find_element_by_xpath('//*[@id="coreAddCartBtn"]')
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.save_screenshot('5_1_hold_purchase.png')
        time.sleep(2)
        element = self.driver.find_element_by_xpath('//*[@id="layer_mycart"]/div/div/div/div[2]/button[2]')
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.save_screenshot('5_2_checking_purchase.png')

    def tear_down(self):
        # 열려있는 window 가져오기
        opened_window_list = self.driver.window_handles

        # 열려있는 모든 window 로그아웃
        index = len(opened_window_list)
        while index:
            self.driver.switch_to_window(opened_window_list[index - 1])
            index = index - 1
            self.driver.find_element_by_xpath('//*[@id="desktop_layout-header"]/div/div/div[2]/div[3]/ul/li[2]/a').click()
            self.driver.save_screenshot(str(index + 6) + '_acoount_logout.png')
            time.sleep(2) # 로그아웃 후 확인을 위해 대기 시간 설정
            self.driver.close()

# TC 구동하기
if __name__ == "__main__":
    # 클래스 ShoppingOnInternet instance 생성
    shopping = ShoppingOnInternet()

    shopping.get_browser()
    shopping.invoke_browser()
    shopping.login_to_homepage()
    shopping.buy_goods()
    shopping.tear_down()
