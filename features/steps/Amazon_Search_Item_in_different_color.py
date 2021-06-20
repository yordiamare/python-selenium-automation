from selenium import webdriver
from selenium.webdriver.common.by import By
from keyboard import press
from behave import given, when, then


@given('Open Amazon Product Page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/')


@when('Search Product On The Search Space')
def search_product_on_search_space(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('EDSTAR Women Dolman Batwing Sleeves Knitted Sweaters Winter Boat Neck Pullovers Tops')


@when('User click Search Button')
def user_click_search_button(context):
    context.driver.find_element(By.ID, "nav-search-submit-button").click()


@when('Click The Needed Product')
def click_the_product_as_needed(context):
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[1]/div/span[3]/div[2]/div[3]/div/span/div/div/div[2]/div/span/a/div/img").click()


@then('Verify User Can Click Through Colors')
def verify_user_can_choose_color(context):
    expected_colors = ['Black', 'Blue', 'Burgundy', 'Caramel', 'Gray', 'Green', 'Khaki', 'Pink', 'White']
    color_options = context.driver.find_elements(By.CSS_SELECTOR, "#variation_color_name li")

    for i in range(len(color_options)):
        color_options[i].click()
        actual_text = context.driver.find_element(By.CSS_SELECTOR, "#variation_color_name span.selection").text
        assert actual_text == expected_colors[i], f'Error, color is {actual_text}, but expected {expected_colors[i]}'