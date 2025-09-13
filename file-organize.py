import os
import shutil

path = input("Enter path: ")
files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]   # remove dot from extension

    if extension == "":   # skip files without extension
        continue

    if os.path.exists(os.path.join(path, extension)):
        shutil.move(os.path.join(path, file), os.path.join(path, extension, file))
    else:
        os.makedirs(os.path.join(path, extension))
        shutil.move(os.path.join(path, file), os.path.join(path, extension, file))
