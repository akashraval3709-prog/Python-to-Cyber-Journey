from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import time

driver=webdriver.Chrome(
    service=Service(
          ChromeDriverManager().install()
                    )
    )

driver.get('https://the-internet.herokuapp.com/checkboxes')

checkboxe=driver.find_elements(By.XPATH,"//input[@type='checkbox']")

time.sleep(2)

if not checkboxe[0].is_selected():
        checkboxe[0].click()
        time.sleep(2)
if checkboxe[1].is_selected():
        checkboxe[1].click()    

time.sleep(2)

driver.get('https://the-internet.herokuapp.com/dropdown')
dropdown_el=driver.find_element(By.ID,"dropdown")
sel=Select(dropdown_el)
time.sleep(2)
sel.select_by_index(1)
time.sleep(2)
sel.select_by_visible_text('Option 2')

input('press Enter key for close Chrome :')
    
driver.quit()
