import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin



user_input = input('Enter your website url for scraping: ')

# Fix URL
if not user_input.startswith('http'):
    user_input = 'https://' + user_input

if '.' not in user_input:
    print('Invalid URL ❌')
    exit()

try:
    start = time.time()
    res = requests.get(user_input, timeout=6)
    end = time.time()

    if res.ok:
        print(f"\nWebsite is UP ✅ (Status: {res.status_code})")

        soup = BeautifulSoup(res.text, 'html.parser')

        # Use stable tag (not random class)
        find_tag=input('Enter you want to find tag : ')
        tags = soup.find_all(find_tag)
        
        headlines = []

        # Extract + Clean
        for tag in tags:
            text = tag.text.strip()

            if text and len(text) > 20:   # small filter (important)
                headlines.append(text)

        # Remove duplicates
        headlines = list(set(headlines))

        print('\n'+'-'*40)
        count=0
       
        for tag in tags:
            text = tag.get_text(strip=True)
            link = tag.get('href')

            # TEXT VALID
            if not text or len(text) < 20:
                continue

            # LINK VALID
            if not link or link in ['#', '/']:
                continue

            # LINK HANDLE
            if link.startswith('http'):
                final_link = link
            elif link.startswith('/'):
                    # base URL fix
                final_link = final_link = urljoin(user_input, link)
            else:
                continue

            # PRINT
            print(f"{text} : {final_link}")
            count += 1

            # LIMIT
            if count == 10:
                break
                
    else:
        print(f"Website issue ❌ (Status: {res.status_code})")

except requests.exceptions.Timeout:
    print("Request timed out ⏱️")

except requests.exceptions.ConnectionError:
    print("Connection Failed ❌")

except requests.exceptions.RequestException:
    print("Some error occurred ❌")
  
  
  
  
  
  
        
