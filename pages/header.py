from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page
from selenium.webdriver.support.ui import Select

# HW 7
class Header(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    ORDERS_LINK = (By.CSS_SELECTOR, "#nav-orders")
    CART_ICON = (By.ID, 'nav-cart-count')
    FLAG = (By.CSS_SELECTOR, ".icp-nav-flag-us")
    SPANISH_LANG = (By.CSS_SELECTOR, "[href='#switch-lang=es_US']")
    DEPARTMENT_SELECT = (By.ID, 'searchDropdownBox')
    DEPARTMENT_SUB_NAV = (By.CSS_SELECTOR, "[data-category='{SUBSTRING}']")
    DEPARTMENT_COM_SELECT = (By.ID, 'searchDropdownBox')
    DEPARTMENT_SUB_NAVIG = (By.CSS_SELECTOR, "[data-category='pc']")


    def get_dept_sub_nav_locator(self, department):
        return [self.DEPARTMENT_SUB_NAV[0], self.DEPARTMENT_SUB_NAV[1].replace('{SUBSTRING}', department)]

    def search_amazon(self, search_word):
        self.input_text(search_word, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)

    def click_orders_link(self):
        self.click(*self.ORDERS_LINK)

    def click_cart_icon(self):
        self.click(*self.CART_ICON)

    def hover_lang(self):
        actions = ActionChains(self.driver)
        flag = self.find_element(*self.FLAG)
        actions.move_to_element(flag)
        actions.perform()

    def select_dept(self, alias):
        department_select = self.find_element(*self.DEPARTMENT_SELECT)
        select = Select(department_select)
        select.select_by_value(f'search-alias={alias}')

    def select_com_dept(self):
        department_comp_select = self.find_element(*self.DEPARTMENT_COM_SELECT)
        select = Select(department_comp_select)
        select.select_by_value('search-alias=computers')

    def verify_spanish_lang(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

    def verify_department(self, department):
        department_locator = self.get_dept_sub_nav_locator(department)
        self.wait_for_element_appear(*department_locator)

    def verify_comp_dept(self):
        self.wait_for_element_appear(*self.DEPARTMENT_SUB_NAVIG)
