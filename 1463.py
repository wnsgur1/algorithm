n = int(input())
c = 0

while(n!=1):

    if n % 2 == 0:
        n = n // 2
        c+=1

    elif n % 3 == 0:
        n = n // 3
        c+=1

    else:
        n -= 1
        c+=1


print(c)