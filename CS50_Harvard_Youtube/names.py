name = input("what's your name? ")

# more automated method for closing files 
with open("names.txt", "a") as file:
    file.write(f"{name}\n")

