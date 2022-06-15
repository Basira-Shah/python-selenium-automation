from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
PRODUCT_PRICE = (By.XPATH, "//span[@class='a-price-whole']")
SEARCH_RESULT_TEXTS = (By.XPATH, "//div[@class='help-content']/h1" )
EMPTY_CART = (By.XPATH, "//h2")




@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()


@then('Verify search result for {expected_result} are shown in the help customer page')
def verify_search_results(context, expected_result):
    actual_result = context.driver.find_element(*SEARCH_RESULT_TEXTS).text
    assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match expected {expected_result}'


@then('Verify search result for {expected_result} are shown')
def verify_search_results(context, expected_result):
    actual_result = context.driver.find_element(*SEARCH_RESULT_TEXT).text
    assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match expected {expected_result}'


@then('Verify your Amazon cart is empty')
def verify_cart_is_empty(context):
    actual_result = context.driver.find_element(*EMPTY_CART).text
    expected_result = 'Your Amazon Cart is empty'
    assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match expected {expected_result}'
