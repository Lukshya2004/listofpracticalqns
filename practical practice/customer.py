import pickle

def addcust():
    file = open("customer.dat", "ab")
    id = int(input())
    name = input()
    email = input()
    record = (id, name, email)

    pickle.dump(record, file)

def search_cust():
    name = input("enter the name of the customer")
    file = open("customer.dat", "rb")
    try:
        while True:
            record = pickle.load(file)
            if record[1] == name:
                print(record)
    
    except EOFError:
        file.close()


