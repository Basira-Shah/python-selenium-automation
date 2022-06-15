from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then, step
from time import sleep
from selenium.webdriver.common.keys import Keys


SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
HAM_MENU_BTN = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, 'td.navFooterDescItem a')
SIGN_IN_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")
SEARCH_FIELD = (By.ID, 'hubHelpSearchInput')
CART_ICON = (By.ID, 'nav-cart-count')



@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@given('Open Amazon help page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('search for {search_word} in help customer page')
def search_amazon(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word, Keys.ENTER)



@when('search for {search_word}')
def search_amazon(context, search_word):
    context.driver.find_element(*SEARCH_INPUT).send_keys(search_word)
    context.driver.find_element(*SEARCH_BTN).click()


@when('click on the cart icon')
def click_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()





#@when('Click on button from SignIn popup')
#def click_sign_in_btn(context):
#    sign_in_btn = context.driver.wait.until(
#        EC.element_to_be_clickable(SIGN_IN_BTN), 'Sign in btn not clickable'
#    )
#    sign_in_btn.click()


#@then('Verify hamburger menu btn present')
#def verify_ham_menu(context):
#    context.driver.find_element(*HAM_MENU_BTN)



@then('Verify there are {expected_amount} footer links')
def verify_footer_links_count(context, expected_amount):
    expected_amount = int(expected_amount) # '38' 38
    footer_links = context.driver.find_elements(*FOOTER_LINKS) # [web elements1, webelements2, ...

    print(type(expected_amount))
    print(type(len(footer_links)))

    assert len(footer_links) == expected_amount, f'Expected {expected_amount} links, but got {len(footer_links)}'



@then('Verify hamburger menu btn present')
def verify_ham_menu(context):
    print('\nUSING FIND ELEMENTS:\n')
    elements = context.driver.find_elements(*HAM_MENU_BTN)
    print(elements)

    print('\nUSING FIND ELEMENT:\n')
    element = context.driver.find_element(*HAM_MENU_BTN)
    print(element)
