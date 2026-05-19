import requests
import threading
import time
import json 


# Duplicate data stop karva mate
seen = set()

# Badha website results store karva mate
results = []


# Website check function
def openWeb(url):

    try:
        # Temporary dictionary
        site_data = {}

        # Response time calculate karva mate
        start = time.time()

        # Website request
        res = requests.get(url, timeout=5)

        end = time.time()

        # ================= WEBSITE UP =================
        if res.ok:

            print('Website UP')

            # Unique key
            key = (url, res.status_code)

            # Duplicate avoid
            if key not in seen:

                seen.add(key)

                # Website data store
                site_data = {

                    "url": url,

                    "state": "UP",

                    "status": res.status_code,

                    "time": f"{end-start:.2f}"
                }

                # Global results ma append
                results.append(site_data)

            # Terminal output
            print(
                f'Url: {url}\t|\tStatus : {res.status_code}\t|\tTime : {end-start:.2f}'
            )

        # ================= WEBSITE DOWN =================
        else:

            print(f'Website is DOWN (Status : {res.status_code})')

            key = (url, res.status_code)

            if key not in seen:

                seen.add(key)

                site_data = {

                    "url": url,

                    "state": "DOWN",

                    "status": res.status_code,

                    "time": f"{end-start:.2f}"
                }

                results.append(site_data)

    # ================= REQUEST FAILED =================
    except requests.exceptions.RequestException:

        print(f'{url} : Failed')

        # Failed data
        site_data = {

            "url": url,

            "state": "FAILED",

            "status": "No Response",

            "time": "Timeout/Error"
        }

        # Failed unique key
        key = (url, "FAILED")

        # Duplicate avoid
        if key not in seen:

            seen.add(key)

            results.append(site_data)


# Website list
sites = [

    "https://www.google.com",

    "https://www.python.org",

    "https://www.github.com",

    "https://www.kali.org",

    "https://www.hackerrank.com"
]


# Thread list
thread_list = []


# Threads create + start
for site in sites:

    t = threading.Thread(
        target=openWeb,
        args=(site,)
    )

    thread_list.append(t)

    t.start()


# Badha threads complete thay tya sudhi wait
for thread in thread_list:

    thread.join()


print('\nAll Websites Checked ✅')


# ================= SUMMARY =================

up_count = 0

down_count = 0

failed_count = 0


# Count websites
for res in results:

    if res['state'] == 'UP':

        up_count += 1

    elif res['state'] == 'DOWN':

        down_count += 1

    else:

        failed_count += 1


print('-' * 40)

print(f'\tUP Websites     : {up_count}')

print(f'\tDOWN Websites   : {down_count}')

print(f'\tFAILED Websites : {failed_count}')


# ================= JSON REPORT =================

with open('report.json', 'w', encoding='utf-8') as f:

    json.dump(results, f, indent=5)


# ================= TEXT REPORT =================

with open('report.txt', 'w', encoding='utf-8') as f:

    for result in results:

        f.write(f"URL : {result['url']}\n")

        f.write(f"State : {result['state']}\n")

        f.write(f"Status : {result['status']}\n")

        f.write(f"Response Time : {result['time']} sec\n")

        f.write('-' * 40 + '\n')


print('\nReports Saved Successfully ✅')
