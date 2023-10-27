n = int(input())
array = list(map(int,input().split()))
c = int(input())


for i in range(0, n, 2):
    array[i], array[i+1] = array[i+1], array[i]
    c-=1
    if (c==0):
        break



for i in array:
    print(i, end=" ")