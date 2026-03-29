import re

email = input("What's your email? ").strip()


if re.search(r"^[^@]+@[^@]+\.edu$", email): # give me something to the left and something to the right. # use the plus sign i.e. at least one character. 
    print("Valid")
else:
    print("Invalid")

# but we must NOT use ".+edu" because it will accept ANY character after . e.g. "aedu" and not ".edu"
# so we need an excape character "\.edu"
# "r" = raw string meaning we want passed in AS IS. 
# good practice to put raw strings into ALL our reguarl expressions even if we don't use it. 

# carrot symbol "^" - matches the start of the string
# "$" end of the string. 
# [^@] any character that is not an @ sign
# re.IGNORECASE allows us to ignore flagged inputs. 