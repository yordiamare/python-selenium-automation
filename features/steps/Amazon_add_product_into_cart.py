from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when('Search Water Bottle On Amazon')
def search_water_bottle_on_the_bar(context):
    context.driver.find_element(By.ID, "twotabsearchtextbox").send_keys('Water Bottle')


@when('Click On Search Button')
def click_search_button(context):
    context.driver.find_element(By.ID, "nav-search-submit-button").click()


@when('Select Water Bottle')
def click_select_water_bottle(context):
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[1]/div/span[3]/div[2]/div[4]/div/span/div/div/div/div/span/a/div/img").click()


@when('Click Add Cart')
def click_add_cart(context):
    context.driver.find_element(By.ID, "add-to-cart-button").click()


@when('Click The Shopping Icon')
def verify_the_shopping_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "span.nav-cart-count").click()


@then('Verify The Subtotal Item')
def verify_the_last_item(context):
    context.driver.find_element(By.XPATH, "//html/body/div[1]/div[4]/div[1]/div[8]/div/div[2]/div[4]/div/form/div[3]/span[1]").click()
