def fileReader(file_path):
    with open(file_path,'r') as file:
         for x in file:
             if 'Error' in x:
                 yield x.strip()

line=fileReader('Akash.txt')
for i in line:
    print(i)