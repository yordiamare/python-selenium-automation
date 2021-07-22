from Pages.base_page import Page

class Main(Page):
    def open_main(self):
        self.open_url(url='https://www.amazon.com/')

    def open_other_url(self):
        self.open_url(url='https://www.google.com')
