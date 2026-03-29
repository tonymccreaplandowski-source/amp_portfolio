names = [] # just a place to gather our names 

with open("names.txt") as file:
    for line in file:
        names.append(line.strip())

# outside the with statement 
for name in sorted(names):
    print(f"hello, {name}") # make sure youre only calling one name and NOT the list itself. 