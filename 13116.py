n = int(input())
for i in range(n):
    aList = []
    bList = []
    a, b = map(int,input().split())
    c = 0
    while(a > 0 and b > 0):
        a = a//2
        b = b//2
        aList.append(a)
        bList.append(b)
    for j in aList:
        for k in bList:
            if j == k and j > c:
                c = j
    print(c*10)
                