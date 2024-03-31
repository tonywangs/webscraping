from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


# # If WebDriver is in your PATH
# # driver = webdriver.Chrome()

# # If WebDriver is not in your PATH, specify its location directly
# driver = webdriver.Chrome(executable_path='/Users/tonywang/Downloads/chromedriver-mac-arm64/chromedriver')

# driver.get("http://www.google.com")

# Specify the path to ChromeDriver and create a Service object
s = Service('/Users/tonywang/Downloads/chromedriver-mac-arm64/chromedriver')

# Use the Service object when creating the Chrome driver instance
driver = webdriver.Chrome(service=s)


search_box = driver.find_element("name", "q")
search_box.send_keys("OpenAI")
search_box.send_keys(Keys.RETURN)

# Import necessary module
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for the results to load
results = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h3"))
)

# Print the titles of the results
for result in results:
    print(result.text)

# Close the browser
driver.quit()
