from selenium.webdriver.common.by import By

from pages.base_page import Page

# HW 7
class SigninPage(Page):
    def verify_url_contains_sign_in_opened(self, url):
        self.verify_url_contains_query(url)


