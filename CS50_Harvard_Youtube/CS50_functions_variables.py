#first program
print("hello, world")

#Inputs
input("What's your name? ")
print("hello, Tony")

#variables
name = input("what's your name? ")
print("hello,") 
print(name)

# Adding Comments
# Ask user for their name
name = input("what's your name? ")

#say hello to user... 
print("hello,") 
print(name)

#more efficient
print("hello, " + name)

#more arguments
print("hello, ", name) #two separate arguments w/ extra space
print("hello,", name) #two arguments w/ no extra space 

#print not end on new line 
print("hello, ", end="")
print(name)

#print overide the the sep argument
print("hello,", name, sep="???") #question marks just to see whats going on

#quotes within quotes
# print(hello, "friend"")
# ^ will call an error. 

# solution number 1 is to use different quotes:
print("hello, 'friend' ")

#solution number 2: backslash 
print("hello, \"friend\"") #using an escape character 

#Fstring
print(f"hello, {name}")

# remove whitespace from str
name = name.strip() # stips off all white space - doesn't fix capitalisation.

# fixing capitalizsation
name = name.capitalize() # only fixes the first letter of the first word e.g. no last name

# Cleaning the code and adding them all together:
name.strip().title()

#strip and title on the first original line:
name = input("what's your name? ").strip().title() #notice that this doesn't strip empty space between each word! 

#split user's name into first name and last name
first, last = name.split(" ") # calling to variables 
#call first name 
print(f" hello, {first}")

#integer work
x = 1
y = 2 
z= x + y 
print(z)

#using different inputs
x = input("whats x? ")
y = input("Whats y? ")

z = x + y

print(z)
# prints 12 because the strings were not turned into integers

#fixing the error using int()
z = int(x) + int(y)

print(z) # prints 3 

#nested function - cleaning the operations
x = int(input("What's x? "))
y = int(input("What's y? "))
print(x + y) # eliminating z 

#floating point vlaues:
x = float(input("What's x? "))
y = float(input("What's y? "))
print(x + y) # produces 4.6 i.e. a float
 
#format string to produce numbers with ","
# from 
x = float(input("What's x? "))
y = float(input("What's y? "))
z= x+y

print(f"{z}") # produces 1000
print(f"{z:,}") # produces 1,000 

# DIVISION
x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y 

print(f"{z}") #produces a long number i.e. 0.6666 (repeating)

# to fix - use round ()
z = round(x  / y, 2) # rounds to 2 digits
print(z)

# using fstring and ".2f" the character we use to tell f strings to round:
print(f"{z: .2f}") #also produces 0.67

# CREATING OUT OWN FUNCTIONS (METHODS) WITH DEF
name = input("What's your name? ")
hello() # this will call an error becasue the function does not exist w/o def
print(name)

# adding def
def hello():
        #everything after the indent is the definition of hello()
        print("hello")

name = input("What's your name? ")
hello() # Now this function simply prints "hello"
print(name) #this function follows to produce "hello  \n  Tony"

# Adding parameter:
def hello(to):
        #adding the parameter to
        print("hello,", to)

name = input("What's your name? ")
hello(name) # now we use the paramter "to" to copy the variable "name" to -> to say "hello" to "to" i.e. name.

# default values to parameters:
def hello(to = "world"):
        #often used incase the user forgets to add somehting in
        print("hello,", to)

hello() # now you can call this function and it will simply produce "hello, world"
name = input("What's your name? ") # but we can still overwrite the default value. 
hello(name)

# Defining MAIN funciton (convention):
# primary functino for saying: "hello, {name}"
def main():
        name = input("What's your name? ")
        hello(name) #using to define but NOT yet calling

#defining but NOT calling
def hello(to = "world"):
        print("hello, ", to)

main()

#now see how this doesn't work: where name ONLY exists in the first function:
def main():
        name = input("What's your name? ")
        hello() # just stating to use this function

#removing default value and trying to pass the variable name
def hello():
        print("hello,", name)

main()
#name exists now ONLY in main() - therefore running name and adding "tony" should throw an error. 

#RETURN VALUES:
def main():
        x = int(input("What's x? "))
        #square the value:
        print("x squared is", square(x)) #note the square function does NOT exist -> this will through an error

#now we define square to provide the functionality:
def square(n):
        return n ** 2

main()

#or using pow()

def square(n):
        return pow(n, 2)

main()