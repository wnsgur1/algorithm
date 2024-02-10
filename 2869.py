a,b,v=map(int,input().split())
dal = (v-b) / (a-b)

if dal%1>0 :

    dal -= (dal % 1)
    dal+=1

dal=int(dal)