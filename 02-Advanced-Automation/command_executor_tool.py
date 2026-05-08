import subprocess

user_input=input('Enter Your command : ')


try:
    res=subprocess.run(['cmd','/c',user_input],capture_output=True,text=True,check=True)
    
except FileNotFoundError:
    print("Error: This command is invalid or not found on your system.")
except subprocess.CalledProcessError as e:
   print("Error output:", e.stderr)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(res.stdout.strip())
