from selenium.webdriver.common.by import By

from pages.base_page import Page

# HW 7
class CartPage(Page):
    EMPTY_CART = (By.CSS_SELECTOR, "h2")

    def verify_cart_is_empty(self, expected_text):
    #    actual_text = self.driver.find_element(*self.EMPTY_CART).text
    #    expected_text = 'Your Amazon Cart is empty'
    #    assert 'Your Amazon Cart is empty' in actual_text, \
    #    f'Expected text {expected_text} is not in {actual_text}'

        self.verify_text(expected_text, *self.EMPTY_CART)


