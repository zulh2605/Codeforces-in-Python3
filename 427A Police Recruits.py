"""
427A - Police Recruits
"""
n=int(input())
event=list(map(int,input().split()))
hold=0
unt=0
for i in event:
    if i>0:
        hold+=i
    else:
        if hold>0:
            hold-=1
        else:
            unt+=1
print(unt)