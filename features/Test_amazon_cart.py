from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\yordi\Automation\python-selenium-automation\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)


driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'nav-cart-count-container').click()

actual_result = driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2").text
expected_result = 'Your Amazon Cart is empty'
assert expected_result == actual_result, f'Expected{expected_result},but got {actual_result}'