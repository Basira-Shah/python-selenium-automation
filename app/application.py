from pages.bestsellers_page import BestsellersPage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.cart_page import CartPage
from pages.signin_page import SigninPage
from pages.product_page import ProductPage

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.bestsellers_page = BestsellersPage(self.driver)
        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.signin_page = SigninPage(self.driver)
        self.product_page = ProductPage(self.driver)