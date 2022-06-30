from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then, step
from time import sleep
from selenium.webdriver.common.keys import Keys


DOG_IMG = (By.CSS_SELECTOR, "#d[alt='Dogs of Amazon']")


@given('Store original window')
def store_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)
    print(context.driver.window_handles)


@when('Click on a dog image')
def click_img(context):
    context.driver.find_element(*DOG_IMG).click()


@when('Switch to a new window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    print("\nAfter click, windows:", context.driver.window_handles)
    all_windows = context.driver.window_handles
    context.driver.switch_to.window(all_windows[1])  # means the index we switch to index 1 the
                                                     # second element

# HW 5 - Removed Sleep
@then('Verify blog is opened')
def verify_blog_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.aboutamazon.com/'))


@then('Close blog')
def close_blog(context):
    context.driver.close()  # here dont use quit becouse it will kill the whole browser
                            # and close will just close the current window


@then('Return to original window')
def return_to_original(context):
    context.driver.switch_to.window(context.original_window)

