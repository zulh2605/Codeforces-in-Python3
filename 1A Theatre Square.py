"""
1A - Theatre Square
"""
import math
n,m,a=input().strip().split()
n=int(n)
m=int(m)
a=int(a)

nCount=math.ceil(n/a)
mCount=math.ceil(m/a)

print(nCount*mCount)