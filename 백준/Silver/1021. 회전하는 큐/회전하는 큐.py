from collections import deque

n, m = map(int, input().split())
targets = list(map(int, input().split()))

queue = deque(range(1, n + 1))
count = 0

for target in targets:
    target_idx = queue.index(target)
    
    left_moves = target_idx
    right_moves = len(queue) - target_idx
    
    if left_moves <= right_moves:
        queue.rotate(-left_moves)
        count += left_moves
    else:
        queue.rotate(right_moves)
        count += right_moves
    
    queue.popleft()

print(count)