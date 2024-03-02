import time
import math
def square_for_num(our_time, num):
    time.sleep(our_time/1000.0)
    result=math.sqrt(num)
    return result
our_num=float(input())
our_time=float(input())
result=square_for_num(our_time, our_num)
print(result)

