"""
231A - Team
"""
n=int(input())
count=0

for _ in range(n):
    decision=list(map(int,input().split()))
    oneCount=0
    for i in decision:
        if i==1:
            oneCount+=1
        if oneCount>1:
            count+=1
            break

print(count)
"""
3
1 1 0
1 1 1
1 0 0 ---> 2


2
1 0 0
0 1 1 ---> 1

"""


