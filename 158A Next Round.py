"""
158A - Next Round
"""
n,k=map(int,input().strip().split())
scorelist=list(map(int,input().strip().split()))
excessCount=0

if(scorelist[k-1])>0:
    for i in scorelist[k:]:
        if(i<=0):
            break
        if i<scorelist[k-1]:
            break
        else:
            excessCount+=1
else:
    for i in reversed(scorelist[:k]):
        if i>0:
            break
        else:
            k-=1
print(k+excessCount)
"""
input
n k
8 5
|10 9 8 7 0|--> 7 5 5
output
6
"""


