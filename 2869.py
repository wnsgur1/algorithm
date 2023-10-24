A,B,V = map(int,input().split())

a = 0
day = 0

while(True):
    day+=1
    a+=A
    if (a>=V):
        break
    a-=B
    
    

print(day)