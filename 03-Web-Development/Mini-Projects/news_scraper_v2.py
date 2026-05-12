import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin
import json

try:
    user_input = input('Enter your website url for scraping: ')
    target_tags = input('Enter tag you want to: ')
    top_limit=int(input('Enter your top limit for screping (Top 10 / 20 / 50 ) : '))
except ValueError:
    print('Enter valid top limit value (integer)')
    exit()
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

        data = []
        seen = set()

        tags = soup.find_all(target_tags)

        print('\n' + '-'*40)
        count = 0
        duplicates_removed = 0
        
        invalid_links=0
        
        for tag in tags:
            text = tag.get_text(strip=True)
            link = tag.get('href')

            # TEXT VALID
            if not text or len(text) < 20:
                continue

            # LINK VALID
            if not link or link in ['#', '/']:
                invalid_links+=1
                continue
             

            # LINK FIX
            if link.startswith('http'):
                final_link = link
                
            elif link.startswith('/'):
                final_link = urljoin(user_input, link)
               
            else:
                invalid_links += 1
                continue

            # DUPLICATE CHECK
            key = (text, final_link)
            if key in seen:
                duplicates_removed+=1
                continue   #skip duplicate

            seen.add(key)

            # STORE DATA
            item = {
                "title": text,
                "link": final_link
            }

            data.append(item)
            print(f"{text} : {final_link}")
            count += 1
           
            if count == top_limit:
                break
           
        print('\nFinal Data:\n', data)
     
        
        with open('news_data2.json','w', encoding='utf-8') as file:
              json.dump(data,file,indent=5)
      
        with open('news.txt','w', encoding='utf-8') as file:
            file.write(f'Website UP ✅')
            file.write('\n' + '-'*40)
            file.write(f'\nStatus Code:{res.status_code}\n')
            file.write(f'Response Time: {(end-start):.2f}\n')
            file.write(f'Total Tags Found:{len(tags)}\n')
            file.write(f'Valid News: {len(data)} \n')
            file.write(f'Duplicates Removed: {duplicates_removed} \n')
            file.write(f'Invalid Links: {invalid_links} \n')
             
    else:
        print(f"Website issue ❌ (Status: {res.status_code})")
    print('\n' + '='*50)

    print(f"Total Tags Found : {len(tags)}")
    print(f"Valid News Collected : {len(data)}")
    print(f"Duplicates Removed : {duplicates_removed}")
    print(f"Invalid Links : {invalid_links}")

    print(f"Response Time : {end-start:.2f} sec")

    print('='*50) 
   

except requests.exceptions.Timeout:
    print("Request timed out ⏱️")

except requests.exceptions.ConnectionError:
    print("Connection Failed ❌")

except requests.exceptions.RequestException:
    print("Some error occurred ❌")
