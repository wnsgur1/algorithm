def move(c):
    global Boxs
    for i in range(len(c)):
        if c[i] >= Boxs[i]:
             Boxs.pop(0)

            

n = int(input())
Crane = list(map(int,input().split()))
Crane.sort(reverse= True)
m = int(input())
Boxs = list(map(int, input().split()))
Boxs.sort(reverse= True)

time = 0

if Boxs[0] > Crane[0]:
        print(-1)
else:
    while len(Boxs) > 0:
        move(Crane)
        time+=1
        break
print(time)
