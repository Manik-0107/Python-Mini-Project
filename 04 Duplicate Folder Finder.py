import os, hashlib

path = input("Please Enter Folder Path: ")
seen = {}

for f in os.listdir(path):
    data = open(os.path.join(path, f), "rb").read()
    h = hashlib.md5(data).hexdigest()
    if h in seen:
        print("Duplicate File: ", f, "<->", seen[h])
    else:
        seen[h] = f
