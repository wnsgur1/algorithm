def fibonacci(n):
    global oneC
    global zeroC
    if n == 0:
        oneC += 1
        return 0
    elif n == 1:
        zeroC += 1
        return 1
    else :
        return fibonacci(n-1) + fibonacci(n-2)


n = int(input())

for i in range(n):
    oneC = 0
    zeroC = 0   
    fibonacci(int(input()))
    print(zeroC, oneC)