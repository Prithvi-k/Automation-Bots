import os

# Change text in path.txt to required path
with open('OS Automations\path_to_file.txt', 'r') as file:
    path = file.read()

files_number = int(input("Please input number of files to be created: "))
files_name = str(input("Please input name of files to be created: "))
files_extension = str(
    input("Please input extension of files to be created (ex: .txt, .docx, .py): "))


if files_extension[0] != '.':
    files_extension = '.' + files_extension
else:
    pass

# Before creating files
dir_list = os.listdir(path)
print("List of directories and files before creation: ")
print(dir_list)
print()

# Creating the files
for i in range(0, files_number):
    if i < 9:
        with open((path + "\\" + files_name + "0" + str(i + 1) + files_extension), 'w') as fp:
            pass
    else:
        with open((path + "\\" + files_name + str(i + 1) + files_extension), 'w') as fp:
            pass

# After creating files
dir_list = os.listdir(path)
print("List of directories and files after creation: ")
print(dir_list)
