from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
# Example: Run headless
# chrome_options.add_argument("--headless")

service = Service('/Users/tonywang/Downloads/chromedriver-mac-arm64/chromedriver')

# Example for Chrome, replace 'chromedriver' with the path to your ChromeDriver
# driver = webdriver.Chrome('/Users/tonywang/Downloads/chromedriver-mac-arm64')
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://weather.com")

search_box = driver.find_element(By.ID, 'searchBox')
search_box.send_keys('New York')
search_box.send_keys(Keys.RETURN)

time.sleep(5)  # Wait for the page to load
temperature = driver.find_element(By.CLASS_NAME, 'current-temp').text
print(f"Current temperature: {temperature}")

driver.close()
