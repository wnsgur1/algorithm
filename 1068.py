n = int(input())
node = list(map(int,input().split()))
dell = int(input())
cnt = 0


for i in range(n):
    if i%2 == 0 and i/2 == dell:
        continue
    elif 1%2!=0 and i/2-1 == dell:
        continue
    else:
        if i*2+1 > n:
            cnt+=1
print(cnt)
