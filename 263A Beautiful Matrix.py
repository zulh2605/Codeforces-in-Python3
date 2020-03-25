"""
263A - Beautiful Matrix
"""
mat=[list(map(int,input().split())) for i in range(5)]

for i,row in enumerate(mat):
    if (1) in row:
        R=i+1
        for j,col in enumerate(row):
            if col==1:
                C=j+1
                break
        break

print(abs(3-R)+abs(3-C))