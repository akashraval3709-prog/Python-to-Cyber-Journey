import subprocess
try:

    res=subprocess.run(['hostname'],capture_output=True,text=True,check=True)
    # print(res.stdout)
    result=subprocess.run(["cmd", "/c", "ver"],capture_output=True,text=True,check=True)
    # print(result.stdout)
except subprocess.CalledProcessError as e:
    print("Error output:", e.stderr)
else:
    print(f'HostName : {res.stdout.strip()}')
    print(f'OS Version.. :{result.stdout.strip()}')
    
    
