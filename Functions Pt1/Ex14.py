# File: my_program.py

from Ex6 import reverse_sentence
from Ex12 import histogram
from Ex11 import is_palindrome

def main():
    sentence = "hello world"
    reversed_sentence = reverse_sentence(sentence)
    print("Reversed sentence:", reversed_sentence)

    word = "madam"
    if is_palindrome(word):
        print(f"'{word}' is a palindrome.")
    else:
        print(f"'{word}' is not a palindrome.")

    int_list = [4, 9, 7]
    print("Histogram:")
    histogram(int_list)

if __name__ == "__main__":
    main()