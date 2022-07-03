from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import Select


class ProductPage(Page):
    NEW_ARRIVALS = (By.CSS_SELECTOR, "a[href='/New-Arrivals/b/?_encoding=UTF8&node=17020138011&ref_=sv_sl_6']")
    WOMEN_IMG = (By.CSS_SELECTOR, "img[src='https://m.media-amazon.com/images/G/01//AMAZON_FASHION/2022/SITE_FLIPS/SPR_22/SUBNAV/W._CB1648157817_.jpg']")

    def open_product(self, product_id):
        self.open_page(f'/dp/{product_id}/')

    def hover_arrivals(self):
        actions = ActionChains(self.driver)
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions.move_to_element(new_arrivals)
        actions.perform()

    def verify_women_image(self):
        self.wait_for_element_appear(*self.WOMEN_IMG)



