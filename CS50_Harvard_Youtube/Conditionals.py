x = int(input("What's x? "))
y = int(input("What's y? "))

#boolean (true or false)
if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")

# elif - don't keep answering questions once we get back a true answer:
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")

# Else - catch all
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

# OR conditional
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# more simple: "are they equal?"
if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")