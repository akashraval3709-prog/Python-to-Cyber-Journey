import subprocess
res=subprocess.run(['ipconfig'],capture_output=True,text=True)
flag=False
lines=res.stdout.splitlines()

for i in lines:
    if 'IPv4 Address'in i:
        ip=i.split(":")[-1].strip()
        print(f"🎯 Your IP Address is: {ip}")
        flag=True
        break   

if not flag:
    print("Could not find the IPv4 Address.")
