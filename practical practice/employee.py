import pickle
print("create file")
print("display info on the file")

choice = int(input("enter choice here: "))

if choice == 1:
    file = open("emp.dat", "ab")
    id = int(input("enter id here: "))
    name = input("enter the name here: ")
    desgn = input("enter their job here: ")
    salary = int(input("enter salary here: "))

    record = (id,name,desgn,salary)

    pickle.dump(record, file)

else:
    file = open("emp.dat", "rb")
    try:
        while True:
            record = pickle.load(file)
            if record[3] > 5000:
                print(record)

    except EOFError:
        file.close()