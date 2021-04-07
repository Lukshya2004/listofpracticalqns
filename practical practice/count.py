file = open("letters.txt", "rb")
for i in file.readlines():
    c = 0 
    for k in i.split():
        if k == "the" or k == "a":
            c += 1
            print(i)
    print(f"the count is {c}")

