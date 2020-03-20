"""
118A - String Task
"""
word=input().lower()
answer=""

for item in word:
    #if consonant
    if item not in ('a','e','i','o','u','y'):
        answer=answer+'.'+item

print(answer)
"""
tourc
.t.r.c

Codeforces
.c.d.f.r.c.s

aBAcAba
.b.c.b

potential best solution
s=input().lower()
for i in "aeiouy":
    s = s.replace(i,"")
print("."+".".join(s))
"""

