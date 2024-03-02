def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines=file.readlines()
        print("Number of lines in the file:", len(lines))
a=input("Get your directories way: ")
count_lines(a)