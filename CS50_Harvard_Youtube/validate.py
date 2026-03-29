email = input("What's your email? ").strip()

username, domain = email.split("@") 

# if username has at least one character its vlaid 
if username and  domain.endswith(".com"): # if user name has a character and if "." is found in domain
    print("Valid")
else:
    print("Invalid")

