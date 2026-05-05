import subprocess

res=subprocess.run(['cmd','/c','tasklist'],capture_output=True,text=True)
if "Notepad.exe" in res.stdout:
    print("Monitoring: Notepad is currently active!")
else:
    print("Status: Notepad is not running.")