a = input().lower()
sa = list(set(a))

li = []
for i in range(len(sa)):
    li.append(a.count(sa[i]))


if li.count(max(li)) > 1:
    print("?")
else:
    print(sa[li.index(max(li))].upper())
