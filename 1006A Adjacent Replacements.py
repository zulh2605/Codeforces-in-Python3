"""
1006A - Adjacent Replacements
"""
n=int(input())
nlist=list(map(int,input().split()))

for i,item in enumerate(nlist):
    if item%2==0:
        nlist[i]-=1

print(' '.join(map(str,nlist)))