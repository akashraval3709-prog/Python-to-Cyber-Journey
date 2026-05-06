import os


user_input = input('Enter your folder path for rename file : ')

if os.path.exists(user_input):
    try:
        files = os.listdir(user_input)
    except FileNotFoundError:
         print("Source folder not found ")
         exit()
         
    count = 1
    for file in files:
        src = os.path.join(user_input, file)

        if os.path.isfile(src):
            fileName, ext = os.path.splitext(file)
            part=fileName.split('_')
            last_part=part[-1]
            
            if last_part.isdigit():
                print(f'⚠️ Skipped (already numbered): {file}')
                continue
            else:
                newFileName = f'{fileName}_{count}{ext}'
                dst = os.path.join(user_input, newFileName)
    
                os.rename(src, dst)
                print(f'✅ Renamed: {file} -> {newFileName}')
                count += 1
               
    print('\n✅ All renaming tasks completed!')
else:
    print('Error: Invalid folder path!')
