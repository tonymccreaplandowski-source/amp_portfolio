# manual loop
"""
print("meow")
print("meow")
print("meow") """ 
# you won't want to copy and past 50 times lol...
# and find a replace would be ardous. 

# while 
"""i = 3
 while #ask a question that MUST be true or false i != 0:
    print("meow")"""

# goes to line one, then line two and three.
# then it goes back to line one to check if the answer is still true. 
# in this case i = 3 will always be true to this particular program will simply continue to run. 
# we perhaps could lose control of the computer this way - undesirable. 
# ctrl + c in the terminal will cancel a program.

"""
i = 3
while i != 0:
    print("meow")
    i = i - 1 # i is being decremented.
"""

# counting up instead of decrementation: 
"""
i = 0 # if this is set to 1, it will count through to 4/
while i < 3: # up to but not through three. 
    print("meow")
    i = i + 1 # copies value from left to right. 
# starting coutning from 0 instead of 1 

# using += instead of of i + 1
i = 0
while i < 3:  
    print("meow")
    i += 1 # shorter script example
"""

# for loop & list 
# for loops allow us to iterate over a list of items. 
"""
for i in [0 , 1, 2]:
    print("meow")
"""

# why might this may not be the best method? 
# think about the extreme?
# what if its not 3 things but 1 million? 
# lets just fix it now

# range(): 
"""
for i in range(1,000,000):
    print("meow")
"""

# PYTHONIC convention if you need a variable place holder but don’t actually need to name it e.g. i or x, or z or y, just name it “_” 
"""
for _ in range(#1,000,000):
    print("meow")
"""

# even shorter - pythonic functionality
"""
print("meow\n" * 3, end="") #escape character and manual end
"""

# getting the USER to tell you how many times the cat meows
# matching an expectiions 
# introduce an infinite loop
# but a way to break out of the loop when we get what we want.
"""
while True:
    n = int(input("What's n? "))
    if n > 0: #want the cat to meow at least one time
        break #stops the loop

for _ in range(n): # and we run the meow
    print("meow")
"""
#this is a VERY common paradigm


# now lets build a meow funciton: 
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? " ))
        if n > 0:
            return n # can use break to get out of the loop but still need to use return to get back a value. 
    
def meow(n):
    for _ in range(n):
        print("meow")

main()