import csv
l=[]
with open("Salaries.csv",mode='r') as file:
    csvfile=csv.reader(file)
    for x in csvfile:
        l.append(x)
print(l)