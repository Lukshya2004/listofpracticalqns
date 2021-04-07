import csv
name = input("enter name")
rollno = int(input("enter rollno here: "))
marks = int(input("enter marks here: "))
with open("12b.csv", "a") as newfile:
    newfilewriter = csv.writer(newfile)
    newfilewriter.writerow([name, rollno, marks])
