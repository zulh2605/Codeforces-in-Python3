"""
122A - Lucky Division
"""
lucky=[4,7,44,47,74,77,444,447,474,477,744,747,774,777]
divisible=False
n=int(input())

if n in lucky:
    divisible=True
else:
    for d in lucky:
        if n%d==0:
            divisible=True
            break

if divisible:
    print("YES")
else:
    print("NO")