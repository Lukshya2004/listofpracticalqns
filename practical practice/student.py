import pickle
print("1. create or append values to the file")
print("2. display all the info on the binary file")
print("3. search for records on the file")

choice = int(input("enter the choice here: "))

if choice == 1:
    file = open("student.dat", "ab")
    name = input("enter the name of the student here: ")
    rollno = int(input("enter rollno here: "))
    record = [rollno,name]
    pickle.dump(record, file)

elif choice == 2:
    file = open("student.dat", "rb")
    try:
        while True:
            record = pickle.load(file)
            print(record)

    except EOFError:
        file.close()

else:
    file = open("student.dat", "rb")
    rollno = int(input("enter the rollno to be searched here: "))
    c = 0 
    try:
        while True:
            record = pickle.load(file)
            if record[0] == rollno:
                print(record)

    except EOFError:
        file.close()


        