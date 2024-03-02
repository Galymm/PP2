import os

def checker(path):
    print("Existnce:", os.path.exists(path))
    print("Readability:", os.access(path, os.R_OK))
    print("Writability:", os.access(path, os.W_OK))
    print("Executability:", os.access(path, os.X_OK))
a=input("Get your directories way: ")
checker(a)