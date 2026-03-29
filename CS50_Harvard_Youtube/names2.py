#reading files that already exist
with open("names.txt", "r") as file: #the read function
    lines = file.readlines() #stores all data into the variable lines

for line in lines:
    print("hello," line.strip()) # the strip() module simple strips all impacts of everything prior and allows only print to act. 

