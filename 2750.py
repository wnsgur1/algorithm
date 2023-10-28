n = int(input())
list = []

for i in range(n):
    list.append(int(input()))

for i in range(n):
    for j in range(n):
        if list[i] < list[j]:
            list[j], list[i] = list[i], list[j]

for i in list:
    print(i)