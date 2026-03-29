# empty list 
students = []

with open("names.csv") as file: #open file and read; change depending on the file you're working with
    for line in file: # for line each line of the file 
        name, house = line.rstrip().split(",") # clean each element of each row and column 
        student = {} # create empty dictionary student 
        student["name"] = name # for each row grab the name element and store it in the name variable
        student["house"] = house # for each row grab the "house" element and store it in the variable house 
        students.append(student) # append to the students list that particuarl student key pair 

# we've now collected all the information but kept track of everything


# same as students2 but instead now we use LAMBDA funciton
for student in sorted(students, key = lambda student: student["name"]): #allows us to use a function without having to actually create one 
    print(f"{student['name']} is in {student['house']}") # when indexing dictionaries we don't use numbers but the name of the key

# sort each dictionary via a key 
# sorted() needs to know how to get the name of they key in order to sort
# so we can quickly define our own function called get_name() which simply returns the name element of the dictionary
# and we pass this function into the sorted function to provide the necessary infomration needed to SORT. 