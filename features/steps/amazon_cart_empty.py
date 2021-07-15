from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon url')
def open_amazon(context):
    #context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()

@when('Click on cart')
def click_cart(context):
    #context.driver.find_element(By.ID, 'nav-cart-count-container').click()
    context.app.Header.click_cart()

@then('Verify Your Amazon Cart is empty')
def verify_cart_empty(context):
    #context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2").text
    actual_result = context.app.Header.verify_cart_empty()
    expected_result = '"Your Amazon Cart is empty"'
    assert expected_result == actual_result, f'Expected{expected_result},but got {actual_result}'