from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then, step
from time import sleep
from selenium.webdriver.common.keys import Keys

TOP_LINKS = (By.CSS_SELECTOR, '#zg_header a')
HEADER = (By.CSS_SELECTOR, '#zg_banner_text')


@given('Open Amazon Bestsellers')
def open_amazon_bestsellers(context):
    # context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
    context.app.bestsellers_page.open_bestsellers()


@then('Verify there are {expected_links} links')
def verify_links_count(context, expected_links):
    # actual_links = context.driver.find_elements(*TOP_LINKS)
    # assert len(actual_links) == int(expected_links), f' Expected {expected_links} links, but got {len(actual_links)}'
    context.app.bestsellers_page.verify_links_present(expected_links)


@then('User can click through top links and verify correct page open')
def click_thru_top(context):
    top_links = context.driver.find_elements(*TOP_LINKS)

    for x in range(len(top_links)):
        link_to_click = context.driver.find_elements(*TOP_LINKS)[x] # here it will find all top links from 0 to 4 and then we click
        link_text = link_to_click.text         # means we search for links every time before clicking on it her link text means for expl bestseller
        link_to_click.click()    # [x] means find the element with index = to iteration that im going for expl the first element
        context.driver.wait.until(EC.element_to_be_clickable(TOP_LINKS))  # will be index 0 and the we will doing the click the second
        header_text = context.driver.find_element(*HEADER).text  # x wil be index 1 will find all the links again so we search for links everytime
        assert link_text in header_text, f'Expected {link_text} to be in {header_text}'  # before clicking on it
