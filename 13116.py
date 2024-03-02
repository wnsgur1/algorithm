n = int(input())

for i in range(n):
    
    aList = []
    bList = []
    a, b = map(int,input().split())
    c = 0
    
    while(a > 0 or b > 0):

        aList.append(a)
        bList.append(b)

        a = a//2
        b = b//2

    for j in aList:
        for k in bList:
            if j == k and j > c:
                c = j
                
    print(c*10)

