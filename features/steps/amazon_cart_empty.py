from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon url')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on cart')
def click_cart(context):
    context.driver.find_element(By.ID, 'nav-cart-count-container').click()

@then('Verify Your Amazon Cart is empty')
def verify_cart_empty(context):
    context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2").text