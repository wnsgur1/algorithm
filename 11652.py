def count(card):
    list = {}

    for i in card:
        if i in list:
            list[i] += 1
        else:
            list[i] = 1

    return list

if __name__ == "__main__":
    n = int(input())
    card = []
    for i in range(n):
        card.append(int(input()))

    cardCnt = count(card)
    resultKey = None
    resultCnt = 0

    for key, val in cardCnt.items():
        if resultCnt < val:
            resultCnt = val
            resultKey = key
        elif resultCnt == val:
            if resultKey is None or resultKey > key:
                resultCnt = val
                resultKey = key

    print(resultKey)