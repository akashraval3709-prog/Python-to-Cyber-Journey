import subprocess

res=subprocess.run(['cmd','/c','dir'],capture_output=True,text=True)
# print(res.stdout)
with open('my_files.txt','w') as file:
    file.write(res.stdout)
    print('Successfully write')

