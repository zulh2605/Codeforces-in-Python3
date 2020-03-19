"""
1A - Theatre Square
"""
import math
n,m,a=input().strip().split()
n=int(n)
m=int(m)
a=int(a)
nCount=0
mCount=0

while n>0:
    n-=a
    nCount+=1

while m>0:
    m-=a
    mCount+=1

print(nCount*mCount)