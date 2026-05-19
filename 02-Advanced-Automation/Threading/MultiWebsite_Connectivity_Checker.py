from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import threading
import time


sites=["https://www.google.com",
       "https://www.python.org",
       "https://www.github.com",
       "https://www.kali.org",
       "https://www.hackerrank.com"]
thread_list = []
start_time=time.perf_counter()
def website_checker(site):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    try:
       driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
       print(f"[Starting] Checking: {site}")
       driver.get(site)
       print(f"[Title] {site} -> {driver.title}")
       time.sleep(2)
    except Exception as e:
        print(f"Error checking {site}: {e}")
    finally:
        
        driver.quit()
        print(f"[Done] {site} !")

for site in sites:
    t=threading.Thread(target=website_checker, args=(site,),daemon=True)
    thread_list.append(t)
    t.start()

for thread in thread_list:
    thread.join()
end_time = time.perf_counter()
print(f"Total Time: {end_time - start_time:.2f}sec")

    
