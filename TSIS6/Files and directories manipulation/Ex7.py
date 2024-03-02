def copy_file(source_path, destination_path):
    with open(source_path, 'r') as source_file, open(destination_path, 'w') as destination_file:
        destination_file.write(source_file.read())
source_file='source.txt'
file_path='destination.txt'
copy_file(source_file, file_path)