# standardizing input regardless of user idiosyncracies 
import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name) # more percise answers

# () we're using the brackets for capturing function 

if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")