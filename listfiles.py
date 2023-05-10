import os

# folder path
dir_path = '.'

# list to store files
files = []
direc = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        files.append(path)
    if os.path.isdir(os.path.join(dir_path, path)):
        direc.append(path)
print(files)
print("")
print(direc)
