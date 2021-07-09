from pages.base_page import page
from selenium.webdriver.common.by import By

class Header(page):
    search_field = (By.ID, '')
    search_icon = (By.ID, '')

    def input_search(self):
        self.input_text('text', *self.search_field)

    def click_search(self):
        self.click(*self.search_icon)
