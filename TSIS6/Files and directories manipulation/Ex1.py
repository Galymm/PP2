import os
def list_of(path):
    print("Directories: ")
    for entry in os.listdir(path):
        print(entry)
    print("\nFiles:")
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            print(entry)
    print("\nAll Directories and Files: ")
    for entry in os.listdir(path):
        print(entry)
a=input("Get your directories way: ")
list_of(a)