from selenium.webdriver.common.by import By
from behave import given, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('Open Amazon T&C page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')
sleep(1)

@when('Store original windows')
def store_window(context):
    context.original_window = context.driver.current_window_handle

sleep(1)

@when('Click on Amazon Privacy Notice link')
def click_on_amazon_privacy_link(context):
    context.driver.find_element(By.XPATH, "//a[@href='https://www.amazon.com/privacy']").click()

sleep(1)

@when('Switch to the newly opened window')
def switch_to_the_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    new_window = context.driver.window_handles[1]
    context.driver.switch_to_window(new_window)

sleep(1)

@then('Verify Amazon Privacy Notice page is opened')
def verify_amazon_privacy_notice_page(context):
    sleep(1)
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ')

sleep(1)

@then('User can close new window and switch back to original')
def close_new_window(context):
    sleep (1)
    context.driver.close