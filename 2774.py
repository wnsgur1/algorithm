n = int(input())
for i in range(n):
    cnt = 1
    list = input()
    a = []
    for i in list:
        a.append(i)

    for j in range(len(a)-1):
        if a[j] != a[j+1]:
            cnt+=1
    print(cnt)