from pages.header import header
from pages.main_page import Main

class application():

    def__init__(self, driver):
        self.driver = driver

        self.main_page = Main(self.driver)
        self.header = header(self.driver)