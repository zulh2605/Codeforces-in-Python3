"""
1139A - Even Substrings
"""
n=int(input())
s=input()
answer=0
for i,subs in enumerate(s):
    if int(subs)%2==0:
        answer+=1+i
print(answer)