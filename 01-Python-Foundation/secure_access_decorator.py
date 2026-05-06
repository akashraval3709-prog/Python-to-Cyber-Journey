def secure_acess(fc):
    def wreppar(*id,**kyarg):
        tokan=input("Enter your token")
        eno=int(input("Enter your eno"))
        if tokan=="Akash10" and  eno==3709:
           return fc(*id,**kyarg)
        else:
         print("❌ Access Denied")
    return wreppar


@secure_acess
def download_data(filename,code):
   print(f"✅{filename} Download the data ...{code}")


download_data("Project_Files.zip",3234)


        

