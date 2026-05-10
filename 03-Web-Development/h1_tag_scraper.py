from bs4 import BeautifulSoup
import requests

user_input = input('Enter your website url for scraping: ')

if not user_input.startswith('http'):
    user_input = 'https://' + user_input

try:
    res = requests.get(user_input)

    if res.ok:
        print(f'Website is UP ✅ (Status: {res.status_code})')

        html = res.text
        soup = BeautifulSoup(html, "html.parser")

        tag = soup.find('h1')

        if tag:
            print(f"H1 Text: {tag.text}")
        else:
            print("No <h1> tag found")

    else:
        print(f"Website is DOWN ❌ (Status: {res.status_code})")

except requests.exceptions.RequestException:
    print("Connection Failed ❌")
