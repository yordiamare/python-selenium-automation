from Pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class Header(Page):
    search_field = (By.ID, 'twotabsearchtextbox')
    search_icon = (By.ID, 'nav-search-submit-button')
    search_cart = (By.ID, 'nav-cart-count-container')
    verify_cart = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2")
    search_order = (By.ID, 'nav-orders')
    verify_sign_in = (By.XPATH, "//div[@class='a-spacing-small']/h1")
    FLAG = (By.CSS_SELECTOR, '.icp-nav-flag.icp-nav-flag-us')
    SPANISH_LANG = (By.CSS_SELECTOR, "a[href='#switch-lang=es_US']")
    DEPARTMENT_SELECT = (By.ID, 'searchDropdownBox')
    Books_department = (By.CSS_SELECTOR, "div#nav-subnav")
    Search_department = (By.ID, 'searchDropdownBox')
    Verify_department = (By.CSS_SELECTOR, "div#nav-subnav")

    def input_search(self):
        self.input_text('Table', *self.search_field)

    def click_search(self):
        self.click(*self.search_icon)

    def click_cart(self):
        self.click(*self.search_cart)

    def hover_flag_icon(self):
        flag = self.find_element(*self.FLAG)
        actions = ActionChains(self.driver)
        actions.move_to_element(flag)
        actions.perform()

    def verify_spanish_lang_present(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

    def verify_books_department(self):
        self.wait_for_element_appear(*self.Books_department)

    def select_department(self):
        select = Select(self.find_element(*self.DEPARTMENT_SELECT))
        select.select_by_value('search-alias=stripbooks')

    def department_search(self):
        select = Select(self.find_element(*self. Search_department))
        select.select_by_value('search-alias=electronics')

    def verify_cart_empty(self):
        self.find_element(*self.verify_cart)

    def click_order(self):
        self.click(*self.search_order)

    def verify_signin_text(self):
        self.find_element(*self.verify_sign_in)

    def input_search_word(self, search_word: str):
        self.input_text(search_word, *self.search_field)

    def verify_department(self):
        self.wait_for_element_appear(*self.Verify_department)