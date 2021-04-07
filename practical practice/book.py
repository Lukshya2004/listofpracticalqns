import pickle
print("create file")
print("display info on the file")

choice = int(input("enter choice here: "))

if choice == 1:
    file = open("book.dat", "ab")
    id = int(input("enter id here: "))
    name = input("enter the name here: ")
    desgn = input("enter author here: ")
    salary = int(input("enter price here: "))

    record = (id,name,desgn,salary)

    pickle.dump(record, file)

else:
    file = open("book.dat", "rb")
    choice = input("enter author here: ")
    c = 0 
    try:
        while True:
            record = pickle.load(file)
            if record[2] == choice:
                c += 1 
                print(record)

    except:
        print(c)
        file.close()

