from selenium.webdriver.common.by import By
from behave import when, then


@when('Click Orders')
def click_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@then('Verify Sign in page opened')
def verify_sign_in_opened(context):
    assert 'https://www.amazon.com/ap/signin' in context.driver.current_url