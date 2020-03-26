"""
236A - Boy or Girl
"""
name=input()
answer=""
while name!="":
    answer=answer+name[0]
    name=name.replace(name[0],"")

if len(answer)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")