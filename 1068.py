
n = int(input())
node = list(map(int,input().split()))
delete = int(input())
cnt = 0
array = []

for i in range(delete, n):
    if i in node:
        node.remove(i)
        
node.remove(delete)

for i in range(len(node)):
    if i in node:
        continue
    else:
        cnt+=1
        
print(cnt)