x, y, w, h = map(int, input().split())

distances = [x, y, w - x, h - y]
print(min(distances))
