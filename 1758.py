def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


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

	# 퀵 정렬
    # line = quick_sort(line)
    # line.reverse()
    # tip = totalTip(line)

    # 파이썬 내장함수 정렬
    line = sorted(line, reverse=True)
    tip = totalTip(line)
    print(tip)
