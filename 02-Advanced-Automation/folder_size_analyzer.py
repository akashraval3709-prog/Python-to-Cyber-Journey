import os

user_input = input('Enter your folder path for scan: ')
files = os.listdir(user_input)

biggest_size = 0
total_size = 0
biggest_file = "No files found"

for file in files:
    file_path = os.path.join(user_input, file)

    if os.path.isfile(file_path):
        current_size = os.path.getsize(file_path)
        total_size += current_size

        print(f"{file} : {current_size / (1024*1024):.2f} MB")

        if current_size > biggest_size:
            biggest_size = current_size
            biggest_file = file

print("\n" + "-" * 40)

print(f"Biggest File : {biggest_file} ({biggest_size / (1024*1024):.2f} MB)")
print(f"Total Size   : {total_size / (1024*1024):.2f} MB")
