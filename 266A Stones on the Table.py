"""
266A - Stones on the Table
"""
n=int(input())
stones=input()
answer=0

if n>1:
    for i in range(1,n):
        if stones[i]==stones[i-1]:
            answer+=1
print(answer)