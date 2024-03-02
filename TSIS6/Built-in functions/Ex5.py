import sys

def checker(elem):
    return all(elem)
n=int(input())
input_values = sys.argv[1:]

bool_tuple=[bool(int(value)) for value in input_values]
result=checker(bool_tuple)
print(result)