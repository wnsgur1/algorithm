a,b=map(int,input().split())
list = []
if a>b:
    print(a-b-1)
    for i in range(b+1,a):
        list.append(i)
elif b>a:
    print(b-a-1)
    for i in range(a+1,b):
        list.append(i)
else:
    print(0)

for i in list:
    print(i, end=' ')
