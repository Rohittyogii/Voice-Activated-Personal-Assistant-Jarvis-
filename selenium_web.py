from selenium import webdriver
from selenium.webdriver.firefox.service import Service

s=Service("C:\\Users\\Rohit\\Desktop\\geckodriver.exe")

class infow():
    def __init__(self):
        self.driver = webdriver.Firefox(service=s)

    def get_info(self, query):
        self.query = query
        self.driver.get("https://www.wikipedia.org")
        search = self.driver.find_element("xpath",'//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element("xpath","/html/body/div[3]/form/fieldset/button")
        enter.click()
