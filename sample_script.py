from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# init driver
driver = webdriver.Chrome(executable_path=r"C:\Users\yordi\Automation\python-selenium-automation\chromedriver.exe")
driver.maximize_window()

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# wait for 4 sec
#sleep(4)
#driver.implicitly_wait(4)

driver.wait = WebDriverWait(driver, 2)
e = driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnk')))

e.click
# click search
#driver.find_element(By.NAME, 'btnK').click()

# verify
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()

