words=[]
n=int(input())

for i in range(n):
    words.append(input())

for i in range(len(words)):
    if len(words[i])>10:
        word=words[i]
        firstchar=word[0]
        secondchar=word[len(word)-1]
        words[i]=firstchar+str(len(words[i])-2)+secondchar
    print(words[i])
