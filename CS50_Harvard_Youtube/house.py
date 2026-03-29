name = input("What's your name? ")

"""
if name == "Harry":
    print("Gryffy")
elif name == "Hermoine":
    print("Gryffy")
elif name == "Ron":
    print("Gryffy")
elif name == "Draco":
    print("Slythy")
else:
    print("Who?")
"""

#redundant and doesn't help solve for complex problems so lets shorten:
"""
if name == "Harry" or name == "Hermoine" or name == "Ron":
    print("Gryffy")
elif name == "Draco":
    print("Slythy")
else:
    print("Who?")
"""
"""
# now using match:
match name: 
    case "Harry":
        print("Gryffy")
    case "Hermoine":
        print("Gryffy")
    case "Ron":
        print("Gryffy")
    case "Draco":
        print("Slythy")
    case _: # our catch all
        print("Who?")
"""

# now shorter using match and "|" as or
match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
        