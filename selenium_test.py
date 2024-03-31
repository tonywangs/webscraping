from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver_path = '/Users/tonywang/Downloads/chromedriver_mac64'  # Update this path
# driver = webdriver.Chrome(executable_path=driver_path)
driver = webdriver.Chrome('/Users/tonywang/Downloads/chromedriver_mac64')


driver.get("http://www.google.com")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("OpenAI")
search_box.send_keys(Keys.RETURN)  # Presses the Enter key

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for the results to appear
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "h3"))
)

# Find the first result and print its title
first_result = driver.find_element(By.CSS_SELECTOR, "h3")
print(first_result.text)

driver.quit()
