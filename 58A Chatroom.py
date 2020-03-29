"""
58A - Chatroom
"""

word=input()
index=-1
count=0
for char in ['h','e','l','l','o']:
    if char in word[index+1:]:
        if word.index(char,index+1)>index:
            index=word.index(char,index+1)
            count+=1
if count==5:
    print("YES")
else:
    print("NO")

    # H = False
    # E = False
    # L1 = False
    # L2 = False
    # O = False
    # if 'h' in word:
    #     word_h = word[word.index('h') + 1:]
    #     H = True
    #     if 'e' in word_h:
    #         word_e = word_h[word_h.index('e') + 1:]
    #         E = True
    #         if 'l' in word_e:
    #             word_l1 = word_e[word_e.index('l') + 1:]
    #             L1 = True
    #             if 'l' in word_l1:
    #                 word_l2 = word_l1[word_l1.index('l') + 1:]
    #                 L2 = True
    #                 if 'o' in word_l2:
    #                     O = True
    #
    # if H and E and L1 and L2 and O:
    #     print("YES")
    # else:
    #     print("NO")