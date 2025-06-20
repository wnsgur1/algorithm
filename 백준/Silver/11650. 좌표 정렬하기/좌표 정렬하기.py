import sys

input = sys.stdin.readline

n = int(input())
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
points.sort()

for i in points:
    print(i[0], i[1])