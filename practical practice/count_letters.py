import os

print("1. create or append values to the file")
print("2. display all the lower case characters")
print("3. display all the upper case characters")
print("4. create a new file")

choice = int(input("enter choice here: "))

if choice == 1:
    file = open("chars.txt", "w")
    words = input("enter info here: ")
    file.write(words)

elif choice == 2:
    lc = 0 
    file = open("chars.txt", "r")
    for i in file.read():
        if i.islower():
            lc += 1 

    print(f"the number of lowercase characters is {lc}")

elif choice == 3:
    uc = 0 
    file = open("chars.txt", "r")
    for i in file.read():
        if i.isupper():
            uc += 1 

    print(f"the number of uppercase characters is {uc}")

elif choice == 4:
    newfile = open("newfile.txt", "w")
    file = open("chars.txt", "r")

    for i in file.readlines():
        if i[0] == "p" or i[0] == "P":
            newfile.write(i)

    os.remove("chars.txt")
    os.rename("newfile.txt", "chars.txt")
