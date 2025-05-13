n = int(input())
d = []

for i in range(n):
    age, name = input().split()
    d.append((int(age), name))


d.sort(key=lambda x: (x[0]))

for i in range(n):
    print(*d[i])