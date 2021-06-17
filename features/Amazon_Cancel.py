from selenium import webdriver
from selenium.webdriver.common.by import By
from keyboard import press

# init driver
driver = webdriver.Chrome(executable_path=r"C:\Users\yordi\Automation\python-selenium-automation\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://www.amazon.com/gp/help/customer/display.html/')

search_field = driver.find_element(By.ID, 'helpsearch')
search_field.send_keys('Cancel order')
#driver.implicitly_wait(15)
press('enter')

actual_text = driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
expected_text = 'Cancel Items or Orders'

assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

driver.quit()


