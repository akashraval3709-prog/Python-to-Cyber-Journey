from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Chrome setup
driver = webdriver.Chrome(
    service=Service(
        ChromeDriverManager().install()
    )
)

# Open website
driver.get("https://www.wikipedia.org")

time.sleep(2)

# First search
search_box = driver.find_element(By.NAME, 'search')

search_box.send_keys('Cyber Security')
# search_box.send_keys('cyber security by python')

time.sleep(1)

search_box.submit()

time.sleep(3)

print(f"\nFirst Page Title : {driver.title}")
print(f"First URL : {driver.current_url}")

# Go back
driver.back()

# IMPORTANT
# Wait for page reload
time.sleep(2)

# Find element AGAIN after back()
search_box = driver.find_element(By.NAME, 'search')

# Clear old text
search_box.clear()

# Check textbox empty or not
print(search_box.get_attribute('value'))

# Second search
search_box.send_keys("Python")

time.sleep(1)

search_box.send_keys(Keys.ENTER)

time.sleep(3)

print(f"\nSecond Page Title : {driver.title}")
print(f"Second URL : {driver.current_url}")

#Go back
driver.back()

# IMPORTANT
# Wait for page reload
time.sleep(2)

search_box=driver.find_element(By.NAME,'search')

search_box.clear()

print(search_box.get_attribute('value'))

#therd search

search_box.send_keys('selenium tutorial')

time.sleep(1)
search_box.send_keys(Keys.ENTER)

time.sleep(3)


print(f"\nSecond Page Title : {driver.title}")
print(f"Second URL : {driver.current_url}")
input('\nPress Enter key to close Chrome : ')

driver.quit()



# python
# cyber security
# selenium tutorial
