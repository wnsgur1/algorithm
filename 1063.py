a = list(input().split())
pan = [[0 for i in range(8)]for i in range(8)]
list = []

print(a[0])
print(a[0][0], a[0][1])
for i in range(ord("A"), ord("I")):
    if a[0][0] == chr(i):
        a[0].remove(0)
        print(a[0])


# for i in range(int(c)):
#     move = input()
#     for j in move:
#         if j == "R":
#             print("R")
#         if j == "L":
#             print("L")
#         if j == "T":
#             print("T")
#         if j == "B":
#             print("B")