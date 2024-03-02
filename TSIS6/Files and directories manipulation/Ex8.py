import os
def del_file(file_path):
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f"File '{file_path}' deleted successfully.")
        except OSError as e:
            print(f"Error: {e}")
    else:
        print(f"File '{file_path}' does not exist.")
file_to_del=input('')
del_file(file_to_del)