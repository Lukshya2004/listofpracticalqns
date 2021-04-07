import pickle
choice = int(input("enter choice here: "))

if choice == 1:
    file = open("phonebook.dat", "wb")
    try:
        while True:
            name = input("enter name of user here: ")
            phoneno = int(input("enter phone here: "))
            record = (name, phoneno)

            pickle.dump(record,file)


    except EOFError:
        file.close()

else:
    file = open("phonebook.dat", "rb")
    try:
        while True:
            record = pickle.load(file)
            if record[0] == "arman":
                print(record)

    except:
        print("arman record does not exist")
        file.close()

