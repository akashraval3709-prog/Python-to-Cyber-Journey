import requests
user_input=input('Enter your website url for screping : ')
if not user_input.startswith('http'):
    user_input='https://'+user_input

try:
    res=requests.get(user_input)
    if res.ok:
        print(f'Website is UP (Status: {res.status_code})')
        size=len(res.text)/1024
        print(f"Page size: {len(res.text)} characters (~{size:.2f} KB)")
    else:
        print(f"Website is DOWN (Status:{res.status_code})" )
except requests.exceptions.RequestException:
     print("Connection Failed")
