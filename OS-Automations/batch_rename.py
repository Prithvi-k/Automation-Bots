import os

search = str(input("Please input file(s) name to be searched and replaced: "))
replace = str(input("Please input name to be renamed to: "))
type_filter = str(input("Please input file type to be searched: "))

# Change text in path.txt to required path
with open('OS Automations\path_to_file.txt', 'r') as file:
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
    # Seperate name from file extension
    doc_name, file_type = os.path.splitext(doc)

    # Filter for files with correct extension
    if type_filter == file_type:
        # Search if search string is in document name
        if search in doc_name:

            # Replace with given text
            new_name = doc_name.replace(search, replace) + file_type
            #os.rename(doc, new_name)
            renamed += 1

            print(f"Renamed file from {doc} to {new_name}")

print(f"Renamed {renamed} files of {len(docs)} files")
