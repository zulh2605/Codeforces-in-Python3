"""
69A - Young Physicist
"""
x=0
y=0
z=0
n=int(input())
vectors=[list(map(int,input().split())) for _ in range(n)]
for i in vectors:
    x+=i[0]
    y+=i[1]
    z+=i[2]

if x==0 and y==0 and z==0:
    print("YES")
else:
    print("NO")
