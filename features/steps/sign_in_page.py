from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    #context.driver.get('https://www.amazon.com')
    context.app.main_page.open_main()


@when('Click Amazon Orders link')
def click_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()

@then('Verify Sign In Page is opened')
def verify_sign_in_page(context):
    context.driver.get('https://www.amazon.com/ap/signin')

