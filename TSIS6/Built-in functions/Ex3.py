def checker(slovo):
    i=''.join(char.lower() for char in slovo if char.isalnum())
    return i==i[::-1]

slovo=input("vashe slovo: ")
result=checker(slovo)
if result==True:
    print("Is palindrome")
if result==False:
    print("Is not palindrome")