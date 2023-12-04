def first(a):
    cnt = 0
    if a%3 == 0:
        a = a//3
        cnt+=1

    while (a != 1):
        if a%3 == 0:
            a = a//3
        elif a%2 == 0:
            a = a//2
        else:
            a-=1
        cnt+=1


    return cnt

def second(a):
    cnt = 0
    if a%2 == 0:
        a = a//2
        cnt+=1

    while (a!= 1):
        if a%3 == 0:
            a = a//3
        elif a%2 == 0:
            a = a//2
        else:
            a-=1
        cnt+=1



    return cnt

def third(a):
    cnt = 1
    a-=1

    while (a!= 1):
        if a%3 == 0:
            a = a//3
        elif a%2 == 0:
            a = a//2
        else:
            a-=1
        cnt+=1



    return cnt

def main():
    
    x = int(input())
    if(x == 1):
        print(x)
    else:
        a = first(x)
        b = second(x)
        c = third(x)

        print((a if a<b else b) if ((b if b<a else a)<c) else c)


main()