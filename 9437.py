while(True):
    t = list(map(int,input().split()))
    delete = 0
    if t[0] == 0:
        break
        
    else:
        for i in range(t[0]//4):
            Page = [2*i+1, 2*i+2, t[0]-2*i-1, t[0]-2*i]
            if t[1] in Page:
                Page.remove(t[1])
                print(*Page)
