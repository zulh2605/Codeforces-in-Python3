n=int(input())
colors=[input() for _ in range(n)]
stones={'purple':'Power','green':'Time','blue':'Space',
        'orange':'Soul','red':'Reality','yellow':'Mind'}
for i in colors:
    del stones[i]

print(len(stones))
for i in stones:
    print(stones[i])