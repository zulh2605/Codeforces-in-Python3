"""
282A - Bit++
"""
n=int(input())
x=0

for _ in range(n):
    command=input()
    if command[1]=='+':
        x+=1
    else:
        x-=1

print(x)