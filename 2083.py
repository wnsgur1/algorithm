while(True):
    name, age, kg = input().split()
    if name == '#':
        break
    if int(age) > 17 or int(kg) >= 80:
        print(name, "Senior")
    else:
        print(name, "Junior")
