def sort(line):
    list = line
    listSize = len(list)
    min = 0
    for i in range(listSize):
        min = i
        for j in range(i+1, listSize):
            if list[min] < list[j]:
                min = j
        list[i], list[min] = list[min], list[i]

    return list

def totalTip(line):
    list = line
    listSize = len(list)    
    for i in range(listSize):
        if list[i]-i > 0:
            list[i] = list[i]-i
        elif list[i]-i <= 0:
            list[i] = 0
        print(list[i])
    return sum(list)

if __name__ == "__main__":
    n = int(input())
    line = []

    for i in range(n):
        line.append(int(input()))

    line = sort(line)
    tip = totalTip(line)

    print(tip)
