print(" // Challenge 6 // ")
import sys

# lets support multiple arguments at prompt
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# take a slice
for arg in sys.argv[1:4]:
    print("Hello, my name is", arg)

print(" // challenge 5 //")

# coding the system to exit early 
# better way of handling errors
# if the user has not given us the data we're looking for
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("Hello, my name is", sys.argv[1])

#import sys and get s0ys.argv
import sys
print(" // Challenge 2 // ")
# pre-empting an error when running the above code e.g. "index out of range"
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Needed a name")


print(" // Challenge 1 // ")
print("hello, my name is", sys.argv[1]) # targeting the first word grabbed ON the prompt line. 
# stored in the SECOND element i.e. not [0].
# the very first element is likely the program name itself. 


print(" // Challenge 3 // ")
# providing more refined error messages; being even more defensive:

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])

# more refined advice

print(" // Challenge 4 // ")
# good practice to keep your primary code and your error handling separate. 
# this challenge is about learning to separate these two functions into distinct blocks of code:

# step 1: check for errors
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")

#step 2: print name tags 
else:
    print("hello, my name is", sys.argv[1]) # however this creates an error because we are still blindly assuming it exists 

