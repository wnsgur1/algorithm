n = int(input())

for i in range(n):
    a = input()
    data = []
    result = 0

    for i in range(len(a)):
        if int(a[i]) not in data:
            result+=1
            data.append(int(a[i]))
    print(result)