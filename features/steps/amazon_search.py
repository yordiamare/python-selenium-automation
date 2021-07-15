from selenium.webdriver.common.by import By
from behave import given, when, then

@given('open Amazon page')
def open_amazon(context):
    #context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()


@when('Input Table in search field')
def search_amazon(context):
    #context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Table')
    context.app.Header.input_search()


@when('Click on Amazon search icon')
def click_search(context):
    #context.driver.find_element(By.ID, 'nav-search-submit-button').click()
    context.app.Header.click_search()


@then('Verify search_worked')
def verify_search_worked(context):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']")
    expected_result = '"Table"'
    assert expected_result == actual_result, f'Expected{expected_result},but got {actual_result}'