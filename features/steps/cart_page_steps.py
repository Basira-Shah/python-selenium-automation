from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, given, then
from time import sleep

CART = (By. ID, 'nav-cart-count')
PRODUCT_NAME = (By.XPATH, "//span[@class='a-truncate-cut']")



@when('Open cart page')
def open_cart_page(context):
    context.driver.get('https://www.amazon.com/cart/smart-wagon?newItems=c0a08eb5-d7af-4b74-bcb8-598d48196e7c,1')


@then('Verify cart has {expected_count} items(s)')
def verify_cart_count(context, expected_count):
    actual_text = context.driver.find_element(*CART).text
    assert expected_count == actual_text, f'Expected {expected_count}, but got {actual_text}'


@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*PRODUCT_NAME).text
    assert context.product_name[:30] in actual_name, f'Expected {context.product_name}