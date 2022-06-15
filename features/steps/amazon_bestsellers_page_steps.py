from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then, step
from time import sleep
from selenium.webdriver.common.keys import Keys

TOP_LINKS = (By.CSS_SELECTOR, '#zg_header a')
HEADER = (By.CSS_SELECTOR, )


@given('Open Amazon Bestsellers')
def open_amazon_bestsellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify there are {expected_links} links in the Bestsellers')
def verify_links_count(context, expected_links):
    actual_links = context.driver.find_elements(*TOP_LINKS)
    assert len(actual_links) == int(expected_links), f' Expected {expected_links} links, but got {len(actual_links)}'