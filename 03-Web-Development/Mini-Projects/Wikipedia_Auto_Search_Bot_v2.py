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

# Search topics
search_topics = ['Cyber Security', 'Python', 'Selenium']

# Open Wikipedia
driver.get("https://www.wikipedia.org")

time.sleep(2)

# Loop through search topics
for item in search_topics:

    # Find search box
    search_box = driver.find_element(By.NAME, 'search')

    # Clear old search
    search_box.clear()

    # Enter search text
    search_box.send_keys(item)

    time.sleep(1)

    # Submit search
    search_box.send_keys(Keys.ENTER)

    time.sleep(2)

    print('\n' + '=' * 70)
    print(f"Search Topic : {item}")
    print(f"Page Title   : {driver.title}")
    print(f"Current URL  : {driver.current_url}")

    # Get all links
    links = driver.find_elements(By.TAG_NAME, 'a')

    print('-' * 70)
    print(f'Total Links Found : {len(links)}')
    print('-' * 70)

    count = 0

    # Print top 10 valid links
    for link in links:

        text = link.text.strip()

        href = link.get_attribute('href')

        # Skip empty links
        if not text or not href:
            continue

        print(f"{text} : {href}")

        count += 1

        if count == 10:
            break

    # Go back to Wikipedia homepage
    driver.back()

    time.sleep(2)

# Close browser
input('\nPress Enter key to close Chrome : ')

driver.quit()
