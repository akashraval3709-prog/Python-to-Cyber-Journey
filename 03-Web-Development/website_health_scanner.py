import requests
import time

user_input = input('Enter your website url for scraping: ')

if not user_input.startswith('http'):
    user_input = 'https://' + user_input
    
if "." not in user_input:
    print("Invalid URL ❌")
    exit()

try:
    start = time.time()
    res = requests.get(user_input, timeout=5)
    end = time.time()

    if res.ok:
        print(f'\nWebsite is UP ✅ (Status: {res.status_code})')

        size_kb = len(res.text) / 1024
        server_name = res.headers.get('server', 'Not Available')
        content_type = res.headers.get('content-type', 'Not Available')
        
       
        print('\n' + '-'*40)
        print(f'Page size    : {len(res.text)} (~{size_kb:.2f} KB)')
        print(f'Server Name  : {server_name}')
        print(f'Content-Type : {content_type}')
        print(f'Response Time: {end - start:.2f} sec')
        print('-'*40)
        print("\nPreview:")
        print(res.text[:200])
        with open('websitereport.txt','a', encoding='utf-8') as f:
            
            f.write("\n" + "="*28+"\n")
            f.write("\t\tWEBSITE SCAN REPORT")
            f.write("\n" + "="*28+"\n")
            f.write("\n" + "-"*40+"\n")
            f.write(f'URL : {user_input}\n')
            f.write(f'Status: {res.status_code}\n')
            f.write(f'Page size    : {len(res.text)} (~{size_kb:.2f} KB)\n')
            f.write(f'Server Name  : {server_name}\n')
            f.write(f'Content-Type : {content_type}\n')
            f.write(f'Response Time: {end - start:.2f} sec\n')
            f.write("-"*40+"\n")
            f.write("Preview:\n")
            f.write(f'{res.text[:200]}\n')
            

    else:
        if res.status_code == 404:
            print("Page Not Found (404)")
        elif res.status_code == 500:
            print("Server Error  (500)")
        else:
            print(f"Website issue  (Status: {res.status_code})")

except requests.exceptions.Timeout:
    print("Request timed out ⏱️")

except requests.exceptions.ConnectionError:
    print("Connection Failed ")

except requests.exceptions.RequestException:
    print("Some error occurred ")
