#build the bricks with copy and paste:
print("#")
print("#")
print("#")

print(" / solution 2 / ")

#using a for loop and iteration:
for _ in range(3):
    print("#")


print(" / solution 3 / ")
# thinking of functions abstractions of complicated ideas 
# allows to think about the function of complicated tasks. 

def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

main()


print(" / solution 4 / ")
#more stream lined and clever approach:

def print_column(height):
    print("#\n" * height, end="")

main()
# main does not need to know that the underlying implentation of print coloumn has changed. 


print(" / solution 5 / ")
# printing the coins 
#abstract away the problem and we solve after:

def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()

print(" / solution 6 / ")
def main():
    print_square(3)
    # start with the abstraction (the guess and figure it out as you go)

def print_square(size):
     #im now defining the new function that takes in a specific "size" i.e. height and width
    # use a loop
    
    # everything starts top to bottom then left to right so we always need to build in this direciton:
    for i in range(size): #for each row in square
        
        for j in range(size): # for each brick in row
            
            # print brick 
            print("#", end="")
        
        print() #

main() 