import csv
file = open("12a.csv", "r")
new = open("12b.csv", "r")
with open("distinction.csv", "w") as newfile:
    newfilewriter = csv.writer(newfile)
    filereader = csv.reader(file)
    for i in filereader:
        if int(i[2]) > 90:
            newfilewriter.writerow(i)

    reader = csv.reader(new)
    for k in reader:
        if int(k[2]) > 90:
            newfilewriter.writerow(k)

