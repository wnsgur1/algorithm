def totalTip(line):
    list = line
    listSize = len(list)    
    for i in range(listSize):
        if list[i]-i > 0:
            list[i] = list[i]-i
        elif list[i]-i <= 0:
            list[i] = 0
    return sum(list)

if __name__ == "__main__":
    n = int(input())
    line = []

    for i in range(n):
        line.append(int(input()))

		# 정렬하고 반전
    line = sorted(line, reverse=True)
    tip = totalTip(line)

    print(tip)
