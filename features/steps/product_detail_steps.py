from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, given, then
from time import sleep


ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
PRODUCT_NAME = (By.ID, 'productTitle')
COLOR_OPTIONS = (By.CSS_SELECTOR, "#inline-twister-expander-content-color_name li[class*='desktop']")
COLOR_NAME = (By.ID, 'inline-twister-expanded-dimension-text-color_name')
DIFFERENT_COLORS = (By.CSS_SELECTOR, "li[id*='color_name']")
Color_Name = (By.CSS_SELECTOR, "#variation_color_name span.selection")


@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    #context.driver.get(f'https://www.amazon.com/dp/{product_id}/')
    context.app.product_page.open_product(product_id)


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    context.driver.wait.until(EC.invisibility_of_element_located(ADD_TO_CART_BTN))


@when('store product name')
def get_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.product_name}')


@when('Hover over New Arrivals')
def hover_arrivals(context):
    context.app.product_page.hover_arrivals()


@then('Verify user can click through colors')
def verify_clicking_colors(context):
    expected_colors = ['Black', 'Solid black', 'Navy']
    actual_colors = []

    color_options = context.driver.find_elements(*COLOR_OPTIONS)
    for option in color_options:
        option.click()
        sleep(2)
        color_name = context.driver.find_element(*COLOR_NAME).text
        actual_colors += [color_name]

    assert actual_colors == expected_colors, f'Error! Expected {expected_colors}, but got {actual_colors}'

# HW 5
@then('Verify user can click different colors')
def verify_clicking_different_colors(context):
    expected_color = ['Army Green', 'Black', 'Blue']
    actual_color = []

    different_colors = context.driver.find_elements(*DIFFERENT_COLORS)
    for color in different_colors[:3]:
        color.click()
        sleep(3)
        colors_name = context.driver.find_element(*Color_Name).text
        actual_color += [colors_name]

    assert actual_color == expected_color, f'Eroor! Expected {expected_color}, but got {actual_color}'

# HW 5
@then('Verify user can see women image option')
def verify_women_image(context):
    context.app.product_page.verify_women_image()