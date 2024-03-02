def count_uppers(slovo):
    count_upper=sum(1 for char in slovo if char.isupper())
    count_lower=sum(1 for char in slovo if char.islower())
    return count_upper, count_lower
slovos=input()
upper, lower=count_uppers(slovos)
print(upper)
print(lower)
