"""
58A - Chatroom
"""
word=input()
H=False
E=False
L1=False
L2=False
O=False

if 'h' in word:
    h=word.index('h')
    H=True
    print("H")
    if 'e' in word[h+1:]:
        e=word.index('e')
        E=True
        print("E")
        if 'l' in word[e+1:]:
            l1=word.index('l')
            L1=True
            print("L1")
            if 'l' in word[l1+1:]:
                l2 = word.index('l')
                L2 = True
                print("L2")
                if 'o' in word[l2+1:]:
                    O=True
                    print("O")
"""""
if H and E and L1 and L2 and O:
    print("YES")
else:
    print("NO")
"""""