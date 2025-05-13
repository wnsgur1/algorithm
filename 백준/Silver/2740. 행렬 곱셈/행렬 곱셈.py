n1, m1 = map(int, input().split())

aList = [list(map(int, input().split())) for _ in range(n1)]

n2, m2 = map(int, input().split())
bList = [list(map(int, input().split())) for _ in range(n2)]
result = [[0 for _ in range(m2)] for _ in range(n1)]


for i in range(n1):
    for j in range(m2):
        for k in range(m1):
            result[i][j] += aList[i][k] * bList[k][j]

for e in result:
    print(*e)
