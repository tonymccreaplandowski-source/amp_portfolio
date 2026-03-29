students = ["harry", "hermoine", "ron"]

# expressing which value you want to grab i.e. index:
print(students[0]) # = harry 

print("/ Task 1 /")

for student in students: 
    print(student) #keep the called variable and not _ # python is ment to be readible . 

print("/ Task 2 / ")
#length function
for i in range(len(students)):
    print(students[i]) # i is location within the list 

print("/ Task 3 / ")
# printing two things i.e. showing index and giving a numebr (outset from 0)
for i in range(len(students)):
    print(i + 1, students[i]) 

print("/ Task 4 / ")
# dict i.e. dictionary -> keys and values ->  something associated with something else 
# more powerful than a list -> two dimensional 
# lets keep track of who belongs to which house 
# only using lists, eventually with complicated lists this would get out of hand fast.

students = {"hermione": "Gryf",
            "harry": "Gryff", 
            "draco": "slyth"
            }

print(students["hermione"]) #dictionaries allow for words as the index instead of numbers 

print("/ Task 5 /")

for student in students:
    print(student, students[student], sep=", ") # this will go to hermioine and get her house and everyone elses house too. 

print("/ Task 6 /")

# lets complicate the problem: 
# and add a third column or association - patronus 
# create a list of dictionary 
# each student is a key value pair 

students = [
    #one dictionary per student
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russle"},
    {"name": "Draco", "house": "Gryffindor", "patronus": None} # to include a value that does not exists = None. 
]

# each dictionary has 3 keys with 3 unique vlaues. 
# now we have accesss to tones of unique values for each student. 

print("/Task 7 /")
for student in students:
    print(student["name"]) # print out all the names of each student. 

print("/Task 8 /")

for student in students:
    print(student["name"], student["house"], student["patronus"], sep = ", ")


