n = int(input())
files = [input() for _ in range(n)]
pattern = ""

for i in range(len(files[0])):
    chars = set(file[i] for file in files)
    if len(chars) == 1:
        pattern += files[0][i]
    else:
        pattern += "?"

print(pattern)
