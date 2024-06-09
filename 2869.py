a,b,v=map(int,input().split())
c = (v-b) % (a-b)
d = (v-b) // (a-b)

if(c == 0):
    print(d)

else:
    print(d+1)