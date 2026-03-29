# asking for someones twitter name -> canonical storing of data, but being flexible with user input 

url = input("URL: ").strip()

# https//www.twitter.com/tonymccrea - lets ignore everything that isn't the account name at the end. 
username = url.replace("https://twitter.com/", "") # find and replace 
print(f"Username: {username}")

# this code can break in many different ways. 

# remmoveprefix :
username = url.removeprefix("https://twitter.com/")

# but lets do this with regular expressions to do this correctly. 
# we're using now re.sub()

import re
url = input("URL: ").strip()

username = re.sub(r"https://twitter.com/", "", url)
print(f"Username: {username}") 

# this  solution is stronger but we can still suffer from corner problems e.g. english to the left of the URL, the http or less than // two slashes. 
# we can start with the ^ to take the start of the input 
# but we also need to fix the "." because otherwise the user could input "?" and it would techincally be valid. 

username = re.sub(r"https?://twitter.com/", "", url) # 0 or 1 of the thing before i.e. the S is optional for HTTP or HTTPS

username = re.sub(r"https?://(www\.)?twitter.com/", "", url) # www. is grouped and optional 

username = re.sub(r"(https?://)?(www\.)?twitter.com/", "", url) # now the WHOLE http:// is optional - grouped and nested!  