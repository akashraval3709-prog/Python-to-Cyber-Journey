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
')
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
