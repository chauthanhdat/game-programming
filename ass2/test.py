from functools import *

a = [1,2,3,4]
b = list(map(lambda x,y: x+y, a[1:], a[:-1]))
print(b)