import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home, state in reader:
        students.append({"name": name, "home": home, "state": state})

for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']} located in {student['state']}")

# can make the code more robust by not assuming the name, home and states will always follow one antoher 
# we can add headers to the data and add csv.DictReader(file)
#then in the append.() we can specify the row names. More robust because it doesn't matter if someone flips the rows and columns 
# becaus we are working with the names.   
# when making assumptions about placement of columns and so forth your code will break fast. 