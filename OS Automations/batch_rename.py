import os

search = str(input("Please input file(s) name to be searched and replaced: "))
replace = str(input("Please input name to be renamed to: "))

# Change text in path.txt to required path
with open('OS Automations\path.txt', 'r') as file:
    path_to_files = file.read()

# Get all files from directory
dirContent = os.listdir(path_to_files)
print(dirContent)
docs = [doc for doc in dirContent if os.path.isfile(
    (path_to_files + "\\" + doc))]
renamed = 0

print(f"{len(docs)} of {len(dirContent)} elements are files.")

# Go through files and check if they match search
for doc in docs:
    if search in doc:

        new_name = doc.replace(search, replace)
        #os.rename(doc, new_name)
        renamed += 1

        print(f"Renamed file from {doc} to {new_name}")

print(f"Renamed {renamed} files of {len(docs)} files")
