a = int(input())
cnt=0

while(a!=1):
    if a%3 == 0:
        a = a//3
    elif a%2 == 0:
        a = a//2
    else:
        a-=1
    cnt+=1
print(cnt)