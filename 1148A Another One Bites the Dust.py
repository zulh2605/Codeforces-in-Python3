"""
1148A - Another One Bites the Dust
"""
a,b,c=map(int,input().split())
print(2*c + 2*min(a,b) + (1 if a>b or b>a else 0) )