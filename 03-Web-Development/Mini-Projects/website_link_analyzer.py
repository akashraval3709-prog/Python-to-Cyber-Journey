import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json
import time

try:
    # USER INPUT
    user_input = input('Enter website URL: ')
    target_tags = input('Enter tag (a/img): ')
    top_limit = int(input('Enter top limit (10/20/50): '))

except ValueError:
    print('Enter valid integer for limit')
    exit()

# URL FIX
if not user_input.startswith('http'):
    user_input = 'https://' + user_input

# URL VALIDATION
if '.' not in user_input:
    print('Invalid URL')
    exit()

try:
    # REQUEST START
    start = time.time()

    res = requests.get(user_input, timeout=5)

    end = time.time()

    if res.ok:

        print(f'\nWebsite is UP ✅ ({res.status_code})')

        soup = BeautifulSoup(res.text, 'html.parser')

        tags = soup.find_all(target_tags)

        # STORAGE
        data = []
        seen = set()

        # COUNTERS
        count = 0
        duplicate = 0
        invalid_links = 0
        internal_links = 0
        external_links = 0

        print('\n' + '-' * 60)

        for tag in tags:

            if count >= top_limit:
                break

            text = tag.get_text(strip=True)

            # LINK EXTRACTION
            if target_tags == 'a':
                link = tag.get('href')

            elif target_tags == 'img':
                link = tag.get('src')

            else:
                continue

            # EMPTY LINK CHECK
            if not link or link in ['#', '/']:
                invalid_links += 1
                continue

            # SHORT TEXT SKIP
            if target_tags == 'a':
                if not text or len(text) < 2:
                    continue

            # URL FIX
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
                duplicate += 1
                continue

            seen.add(key)

            # INTERNAL / EXTERNAL
            if final_link.startswith(user_input):
                link_type = 'internal'
                internal_links += 1

            else:
                link_type = 'external'
                external_links += 1

            # STORE DATA
            item = {
                "text": text,
                "link": final_link,
                "type": link_type
            }

            data.append(item)

            print(f'{text} : {final_link}')

            count += 1

        # JSON SAVE
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=5)

        # TXT REPORT SAVE
        with open('report.txt', 'w', encoding='utf-8') as file:

            file.write('=' * 50 + '\n')
            file.write('WEBSITE LINK ANALYZER REPORT\n')
            file.write('=' * 50 + '\n\n')

            file.write(f'URL : {user_input}\n')
            file.write(f'Status Code : {res.status_code}\n')
            file.write(f'Response Time : {end - start:.2f} sec\n\n')

            file.write(f'Total Tags Found : {len(tags)}\n')
            file.write(f'Collected Links : {len(data)}\n')
            file.write(f'Internal Links : {internal_links}\n')
            file.write(f'External Links : {external_links}\n')
            file.write(f'Duplicate Removed : {duplicate}\n')
            file.write(f'Invalid Links : {invalid_links}\n')

        # FINAL REPORT
        print('\n' + '=' * 50)

        print(f'Total Tags Found : {len(tags)}')
        print(f'Collected Links : {len(data)}')
        print(f'Internal Links : {internal_links}')
        print(f'External Links : {external_links}')
        print(f'Duplicate Removed : {duplicate}')
        print(f'Invalid Links : {invalid_links}')

        print(f'Response Time : {end - start:.2f} sec')

        print('=' * 50)

        print('\nData saved in:')
        print('✔ data.json')
        print('✔ report.txt')

    else:
        print(f'Website issue ❌ ({res.status_code})')

# ERROR HANDLING

except requests.exceptions.Timeout:
    print('Request timed out ⏱️')

except requests.exceptions.ConnectionError:
    print('Connection Failed ❌')

except requests.exceptions.RequestException:
    print('Some error occurred ❌')
