from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.google.com")
links=driver.find_elements(By.TAG_NAME,'a')

print(f'number of links : { len(links)}')

for i in range(len(links)):
    if i==5:
        break
    print(f"{links[i].text} : {links[i].get_attribute('href')}")
    
links=driver.find_elements(By.CLASS_NAME,'akash-xyz')

print(f'number of class : { len(links)}')

