import string

def generate_text_files():
    for letter in string.ascii_uppercase:
        file_name = letter + '.txt'
        with open(file_name, 'w') as file:
            file.write(f'This is file {letter}')
generate_text_files()