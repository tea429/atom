import os
PATH = os.getcwd()
for root, subdirs, files in os.walk(os.getcwd()):
    head, tail = os.path.split(PATH)
    for file in files:
        print(file)
