from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.wikipedia.org")
time.sleep(2)

search_box=driver.find_element(By.NAME , 'search')

search_box.send_keys('python')
search_box.submit()

time.sleep(2)
driver.back()




search_box=driver.find_element(By.NAME , 'search')
time.sleep(2)
search_box.clear()
print(search_box.get_attribute('value'))
search_box.send_keys('Cyber Security')
# search_box.send_keys(Keys.TAB)
search_box.send_keys(Keys.ENTER)
 
# enter_button=driver.find_elements(By.XPATH,"//button[@type='submit']")
# enter_button.click()
time.sleep(2)

# enter_button.se



input('press Enter key for close Chrome :')
driver.quit()
