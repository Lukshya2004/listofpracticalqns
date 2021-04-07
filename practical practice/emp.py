import pickle
def createbin():
    file = open("employee.dat", "ab")
    id = input("enter id here")
    name = input("enter name here")
    salary = int(input("enter salary here"))
    record = (id,name,salary)
    pickle.dump(record, file)

def readbin():
    file = open("employee.dat", "rb")
    try:
        while True:
            record = pickle.load(file)
            print(record)

    except EOFError:
        file.close()

def disp_sal():
    file = open("employee.dat", "rb")
    try:
        while True:
            record = pickle.load(file)
            if record[2] > 25000 and record[2] < 30000:
                print(record)

    except EOFError:
        file.close()


