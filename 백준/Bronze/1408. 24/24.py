now = list(map(int, input().split(":")))
start = list(map(int, input().split(":")))


now_sec = now[0] * 3600 + now[1] * 60 + now[2]
start_sec = start[0] * 3600 + start[1] * 60 + start[2]

if start_sec >= now_sec:
    diff = start_sec - now_sec
else:
    diff = (24 * 3600 - now_sec) + start_sec

h = diff // 3600
diff %= 3600
m = diff // 60
s = diff % 60

print(f"{h:02d}:{m:02d}:{s:02d}")
