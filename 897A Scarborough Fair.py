"""
897A - Scarborough Fair
"""
n,m=map(int,input().split())
s=input()
for _ in range(m):
    l,r,c1,c2=input().split()
    l=int(l)
    r=int(r)
    if c1 in s[l-1:r]:
        s=s[:l-1]+s[l-1:r].replace(c1,c2)+s[r:]

print(s)