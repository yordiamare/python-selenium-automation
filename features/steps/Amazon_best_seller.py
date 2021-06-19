from selenium.webdriver.common.by import By
from behave import given, then

@given('Open Amazon Best Seller Page')
def open_amazon_help(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@then('Verify Best Seller Link')
def verify_best_seller(context):
    best_seller_text = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/ul/li[1]/div/a").text
    expected_text = 'Best Sellers'
    assert expected_text == best_seller_text, f'Expected {expected_text}, but got {best_seller_text}'

@then('Verify New Release Link')
def verify_new_release(context):
    new_release_text = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/ul/li[2]/div/a").text
    expected_2nd_text = 'New Releases'
    assert expected_2nd_text == new_release_text, f'Expected {expected_2nd_text}, but got {new_release_text}'

@then('Verify Movers & Shakers')
def verify_Movers_Shakers(context):
    movers_shakers_text = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/ul/li[3]/div/a").text
    expected_3rd_text = 'Movers & Shakers'
    assert expected_3rd_text == movers_shakers_text, f'Expected {expected_3rd_text}, but got {movers_shakers_text}'

@then('Verify Most Wished For')
def verify_most_wished_for(context):
    most_wished_text = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/ul/li[4]/div/a").text
    expected_4th_text = 'Most Wished For'
    assert expected_4th_text == most_wished_text, f'Expected {expected_4th_text}, but got {most_wished_text}'

@then('Verify Gift Areas')
def Verify_gift_areas(context):
    gift_ideas_text = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/ul/li[5]/div/a").text
    expected_5th_text = 'Gift Ideas'
    assert expected_5th_text == gift_ideas_text, f'Expected {expected_5th_text}, but got {gift_ideas_text}'