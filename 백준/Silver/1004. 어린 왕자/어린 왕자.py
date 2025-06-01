import sys
input = sys.stdin.readline

def inside(x, y, cx, cy, r):
    return (x - cx) ** 2 + (y - cy) ** 2 < r ** 2

T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        start_in = inside(x1, y1, cx, cy, r)
        end_in = inside(x2, y2, cx, cy, r)
        if start_in != end_in:
            cnt += 1
    print(cnt)
