from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME, 'q')
button=driver.find_element(By.XPATH,"//input[@value=\"I'm Feeling Lucky\"]")
tag_name=driver.find_elements(By.TAG_NAME,'a')
print(f'search_box : {search_box}')
print(f"Search Box Name: {search_box.get_attribute('name')}")
print(f'NUmber of links : {len(tag_name)}')  
 

input('press Enter key for close Chrome :')
driver.quit()
