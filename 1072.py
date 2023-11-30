a,b = map(int,input().split())
z1 = b/a*100
z2 = z1
cnt= 0
while(int(z1) == int(z2)):
    cnt+=1
    b+=1
    z1 = b/a*100
print(cnt)