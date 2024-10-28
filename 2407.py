def factorial(a):
    b = 1
    for i in range(1, a+1):
        b *= i

    return b


n, r = map(int, input().split())

a = factorial(r)
b = factorial(n)
c = factorial(n-r)
result = b//(c*a)


print(result)