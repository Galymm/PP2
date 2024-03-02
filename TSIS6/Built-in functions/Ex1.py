def multiplay(number):
    result=1
    for i in number:
        result*=i
    return result
n=int(input())
numbers=[]
for i in range(n):
    x=int(input())
    numbers.append(x)

print(multiplay(numbers))