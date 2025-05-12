a = int(input())

for i in range(a):
    s = str(i)
    padding = ['0'] * (len(str(a)) - len(s))
    c = padding + list(s)
    vv = sum(int(e) for e in c)
    if vv+i== a:
        print(i)
        exit()

print(0)