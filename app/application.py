from Pages.amazon_header import Header
from Pages.Main_page import Main

class application:

    def __init__(self, driver):
        self.driver = driver

        self.main_page = Main(self.driver)
        self.Header = Header(self.driver)