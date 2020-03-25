"""
112A - Petya and Strings
"""
wordA=input().lower()
wordB=input().lower()
answer=0
for i in range(len(wordA)):
    if wordA[i]<wordB[i]:
        answer=-1
        break
    elif wordA[i]>wordB[i]:
        answer=1
        break

print(answer)