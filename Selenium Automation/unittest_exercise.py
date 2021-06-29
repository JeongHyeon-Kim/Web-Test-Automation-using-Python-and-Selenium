import unittest
import time
from selenium import webdriver

class SearchProducts(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.gmarket.com/")
        self.driver.maximize_window()

    def testSearchByCategory(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("keyword")
        self.search_field.clear()
        # enter search keyword and submit
        # use search_value argument to pass data
        self.search_field.send_keys(u"phones")
        self.search_field.submit()
        
        time.sleep(2)

        # get all the anchor elements which have product names displayed
        list_item = self.driver.find_elements_by_tag_name("li")

        # check count of products shown in results
        self.assertEqual(2, len(list_item)) # AssertionError: 2 != 411

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
        
