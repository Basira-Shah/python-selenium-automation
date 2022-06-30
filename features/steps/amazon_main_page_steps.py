from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then, step
from time import sleep
from selenium.webdriver.common.keys import Keys


SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
HAM_MENU_BTN = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, 'td.navFooterDescItem a')
SIGN_IN_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")
SEARCH_FIELD = (By.ID, 'hubHelpSearchInput')
CART_ICON = (By.ID, 'nav-cart')
SEARCH_RESULT = (By.CSS_SELECTOR, "div[data-component-type=s-search-result]")
PRODUCT_TITLE = (By.CSS_SELECTOR, "h2 span.a-text-normal")
PRODUCT_IMG = (By.CSS_SELECTOR, "img[data-image-latency='s-product-image']")
ORDERS_LINK = (By.CSS_SELECTOR, "#nav-orders")


@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main_page()


@given('Open Amazon help page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('search for {search_word} in help customer page')
def search_amazon(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word, Keys.ENTER)


@when('search for {search_word}')
def search_amazon(context, search_word):
    # context.driver.find_element(*SEARCH_INPUT).send_keys(search_word)
    # context.driver.find_element(*SEARCH_BTN).click()
    context.app.header.search_amazon(search_word)


@when('click on the cart icon')
def click_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()


@when('Wait for {seconds} seconds')
def wait_sec(context, seconds):
    sleep(int(seconds))


@when('Hover over language options')
def hover_lang(context):
    context.app.header.hover_lang()


@when('Select department by {alias}')
def select_dept(context, alias):
    context.app.header.select_dept(alias)


@when('Select computers department')
def select_com_dept(context):
    context.app.header.select_com_dept()


@when('Click on button from SignIn popup')
def click_sign_in_btn(context):
    sign_in_btn = context.driver.wait.until(
        EC.element_to_be_clickable(SIGN_IN_BTN), 'Sign in btn not clickable'
    )
    sign_in_btn.click()


@when('Click Amazon Orders link')
def click_orders_link(context):
    #context.driver.find_element(*ORDERS_LINK).click()
    context.app.header.click_orders_link()


@then('Verify hamburger menu btn present')
def verify_ham_menu(context):
    ham_menu = context.driver.find_element(*HAM_MENU_BTN)  # first find then click you can not refresh it before clicking
    ham_menu.click()
    context.driver.refresh()   # here can i use it or not


@then('Verify there are {expected_amount} footer links')
def verify_footer_links_count(context, expected_amount):
    expected_amount = int(expected_amount) # '38' 38
    footer_links = context.driver.find_elements(*FOOTER_LINKS) # [web elements1, webelements2, ...

    print(type(expected_amount))
    print(type(len(footer_links)))

    assert len(footer_links) == expected_amount, f'Expected {expected_amount} links, but got {len(footer_links)}'



#@then('Verify hamburger menu btn present')
#def verify_ham_menu(context):
#    print('\nUSING FIND ELEMENTS:\n')
#    elements = context.driver.find_elements(*HAM_MENU_BTN)
#    print(elements)

#    print('\nUSING FIND ELEMENT:\n')
#    element = context.driver.find_element(*HAM_MENU_BTN)
#    print(element)


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULT)
    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Error! Title should not be blank'
        product.find_element(*PRODUCT_IMG)


@then('SignIn popup is present')
def verify_signin_popup_present(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BTN), 'Sign in btn not clickable')


@then('SignIn popup disappears')
def verify_signin_popup_not_present(context):
    context.driver.wait.until_not(EC.element_to_be_clickable(SIGN_IN_BTN), 'Sign in btn did not disappear')


@then('Verify Spanish option present')
def verify_spanish_lang(context):
    context.app.header.verify_spanish_lang()


@then('Verify {department} department is selected')
def verify_department(context, department):
    context.app.header.verify_department(department)


@then('Verify computers departments is selected')
def verify_comp_dept(context):
    context.app.header.verify_comp_dept()