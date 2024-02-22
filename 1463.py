n = int(input())

list1 = [0 for i in range(n+1)]

for i in range(1, n):
    list2 = []
    list2.append(list1[i-1]+1)

    if i%2 == 0:
        list2.append(list1[i//2]+1)

    if i%3 == 0:
        list2.append(list1[i//3]+1)
        
    list1.pop(i)
    list1.insert(i, min(list2))
    
    print(list2)


print(list1[-2]+1)