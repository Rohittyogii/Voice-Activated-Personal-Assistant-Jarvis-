from selenium import webdriver
from selenium.webdriver.firefox.service import Service

s = Service("C:\\Users\\Rohit\\Desktop\\geckodriver.exe")

class MusicPlayer:
    def __init__(self):
        self.driver = webdriver.Firefox(service=s)

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        video = self.driver.find_element("xpath",'//*[@id="contents"]/ytd-item-section-renderer[1]')
        video.click()

