import pickle
def create_file():
    file = open("stud.dat","ab")
    name = input("enter the name here: ")
    rollno = int(input("enter the rollno here: "))
    marks = int(input("enter the marks of the student here: "))
    record = [name, rollno, marks]
    pickle.dump(record, file)

def read_info():
    file = open("stud.dat", "rb")
    try:
        while True:
           record = pickle.load(file)
           if record[2] < 40:
               print(record)

    except EOFError:
        file.close()

def search_info(filename, rollno):
    file = open(filename, "rb")
    choice = int(input("enter rollno here: "))
    try:
        while True:
            record = pickle.load(file)
            if record[1] == choice:
                print(record)

    except:
        file.close()




