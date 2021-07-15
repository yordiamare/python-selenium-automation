from Pages.base_page import Page
from selenium.webdriver.common.by import By

class Header(Page):
    search_field = (By.ID, 'twotabsearchtextbox')
    search_icon = (By.ID, 'nav-search-submit-button')
    search_cart = (By.ID, 'nav-cart-count-container')
    verify_cart = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2")
    search_order = (By.ID, 'nav-orders')
    verify_sign_in = (By.XPATH, "//div[@class='a-spacing-small']/h1")

    def input_search(self):
        self.input_text('Table', *self.search_field)

    def click_search(self):
        self.click(*self.search_icon)

    def click_cart(self):
        self.click(*self.search_cart)

    def verify_cart_empty(self):
        self.find_element(*self.verify_cart)

    def click_order(self):
        self.click(*self.search_order)

    def verify_signin_text(self):
        self.find_element(*self.verify_sign_in)