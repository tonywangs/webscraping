from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Set the path to your ChromeDriver
s = Service('/Users/tonywang/Downloads/chromedriver-mac-arm64')

# Instantiate the WebDriver with the Service object
driver = webdriver.Chrome(service=ChromeDriverManager().install())

# Now, the rest of your script can remain the same
# Open Google
driver.get("http://www.google.com")

# Find the search box using its name attribute value
search_box = driver.find_element("name", "q")

# Type 'Selenium HQ' in the search box
search_box.send_keys('Selenium HQ')

# Press ENTER to submit the search
search_box.send_keys(Keys.RETURN)

# Wait a bit for search results to appear
driver.implicitly_wait(5) # seconds

# Print the title of the page
print(driver.title)

# Close the browser
driver.quit()

