import os

def check_path_and_get_info(path):
    if os.path.exists(path):
        print("Path exists.")
        dirname, filename=os.path.split(path)
        print("Directory:", dirname)
        print("Filename:", filename)
    else:
        print("Path does not exist.")
a=input("Get your directories way: ")
check_path_and_get_info(a)
    