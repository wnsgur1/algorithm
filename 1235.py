n = int(input())
list = []
for i in range(n):
    a = input()
    list.append(a)

b=1

while(1):
    if len({i[-b:]for i in list}) == n:
        print(b)
        break
    b+=1
