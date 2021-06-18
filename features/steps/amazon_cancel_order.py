from selenium import webdriver
from selenium.webdriver.common.by import By
from keyboard import press
from behave import given, when, then

@given('Open Amazon Help page')
def open_amazon_help(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/')

@when('Search library')
def Search_library(context):
    context.driver.find_element(By.ID, 'helpsearch').send_keys('cancel order')
    press('enter')
@when('User type cancel order')
def User_type_cancel_order(context):
    context.driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text