#from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon Site')
def open_amazon(context):
    #context.driver.get('https://www.amazon.com')
    context.app.main_page.open_main()


@when('Click Amazon Orders link')
def click_orders(context):
    #context.driver.find_element(By.ID, 'nav-orders').click()
    context.app.Header.click_order()


@then('Verify Sign In Page is opened')
def verify_sign_in_page(context):
    #context.driver.get('https://www.amazon.com/ap/signin')
    actual_result = context.app.Header.verify_signin_text()
    expected_result = '"Sign-In"'
    assert expected_result == actual_result, f'Expected{expected_result},but got {actual_result}'
