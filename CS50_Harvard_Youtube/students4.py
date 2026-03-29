#  using students.csv is designed to throw and error
# in this csv we have 3 key value pairs and not two such as in name.csv 
# we will learn to overcome this now 
# the commas in a CSV dileniate between the different values- therefore we get a value error
# too many values. 

# empty list 
students = []

with open("students.csv") as file: #open file and read; change depending on the file you're working with
    for line in file: # for line each line of the file 
        name, house = line.rstrip().split(",") # clean each element of each row and column 
        student = {} # create empty dictionary student 
        student["name"] = name # for each row grab the name element and store it in the name variable
        student["house"] = house # for each row grab the "house" element and store it in the variable house 
        students.append(student) # append to the students list that particuarl student key pair 

for student in sorted(students, key = lambda student: student["name"]): 
    print(f"{student['name']} is from {student['house']}") 