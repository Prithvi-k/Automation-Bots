import os
import argparse

parser = argparse.ArgumentParser(description="Batch rename files in directory")

parser.add_argument("search", type=str, help="To be replaced text")
parser.add_argument("replace", type=str, help="Text to use for replacement")
parser.add_argument(
    "--filetype",
    type=str,
    default=None,
    help="Only files with given type will be renamed (e.g. .txt, .doc, .jpg)"
)
parser.add_argument(
    "--path",
    type=str,
    default=".",
    help="Directory path that contains the files to be renamed"
)

args = parser.parse_args()

search = args.search
replace = args.replace
type_filter = args.filetype
path = args.path

print(f"Renamed files at path {path}")

# Get all files from directory
dir_content = os.listdir(path)
path_dir_content = [os.path.join(path, doc) for doc in dir_content]
docs = [doc for doc in path_dir_content if os.path.isfile(doc)]
renamed = 0

print(f"{len(docs)} of {len(dir_content)} elements are files.")

# Go through files and check if they match search
for doc in docs:
    # Seperate name from file extension
    full_doc_path, filetype = os.path.splitext(doc)
    doc_path = os.path.dirname(full_doc_path)
    doc_name = os.path.basename(full_doc_path)

    # Filter for files with correct extension
    if filetype == type_filter or type_filter == None:
        # Search if search string is in document name
        if search in doc_name:
            # Replace with given text
            new_doc_name = doc_name.replace(search, replace)
            new_doc_path = os.path.join(doc_path, new_doc_name) + filetype
            os.rename(doc, new_doc_path)
            renamed += 1

            print(f"Renamed file from {doc} to {new_doc_path}")

print(f"Renamed {renamed} files of {len(docs)} files")
