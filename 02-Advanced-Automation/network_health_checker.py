import subprocess

sites=['Google.com', 'GitHub.com','Facebook.com','linkedin.com']
# sites=input('Enter your sites for ping :')

for site in sites:
        test=subprocess.run(['ping','-n','1',site],capture_output=True,text=True)
        if test.returncode==0:
            print(f'Online : {site} ')
        else:
            print(f'Offline : {site} ')
