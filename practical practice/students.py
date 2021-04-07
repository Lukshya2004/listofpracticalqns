import pickle

def createfile():
    file = open("students.dat", "ab")
    no = int(input("enter adm no here: "))
    name = input("enter student name here: ")
    percentage = int(input("enter marks here: "))
    record = (no, name, percentage)

    pickle.dump(record, file)

def countrec(filename):
    file = open(filename,"rb")
    try:
        while True:
            record = pickle.load(file)
            if record[2] > 75:
                print(record)

    except EOFError:
        file.close()
