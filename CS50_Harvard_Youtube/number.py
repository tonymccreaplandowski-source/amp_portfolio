print(" \ Problem 1 \ ")
#prompt for integer and print
x = int(input("what's x? "))
print(f"x is {x}") #interpolating x the variable 

# What could go wrong here? How can we defenisively create the same problem.
# lets try corner cases, 0 and - numbers or a string like "cat".

# try and accept
print("\ Problem 2 \ ")

#NAME ERROR CODE:
"""
try: 
    x = int(input("what's x? "))
    print(f"x is {x}") #interpolating x the variable   
except ValueError:
    print("x is not an integer")

print(f"x is {x}")
"""
# Else solution: 
print(" \ solution 3 \ ") 
try: 
    x = int(input("what's x? "))
    print(f"x is {x}") #interpolating x the variable   
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

#using loops to reprompt:
print(" \ problem 4 \ ") 

while True:
    try:
        x = int(input("What's x? ")) #try to get an input and turn it into an integer
    except ValueError:
        print("x is not an integer") #if no probelsm; otherwise we loop
    else:
        break # we exit; which is needed to break out. 

print(f"x is {x}")

# make a funciton and retunr the value:
print(" \ problem 5 \ ")
def main():
    x = get_int() #abstracted away the working i.e. hide it behind a function.
    print(f"x is {x}") 

def get_int():
    while True:
        try:
            x = int(input("What's x? ")) 
        except ValueError:
            print("x is not an integer") 
        else:
            return x #return is both a break and return! 

main() # no matter what we invoke main. 

# make a funciton and retunr the value:
print(" \ problem 6 \ ")
def main():
    x = get_int() #abstracted away the working i.e. hide it behind a function.
    print(f"x is {x}") 

def get_int():
    while True:
        try:
            return int(input("What's x? ")) # shorter 
        except ValueError:
            pass #stay in the loop 

main() # no matter what we invoke main. 