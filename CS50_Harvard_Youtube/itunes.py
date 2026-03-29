# apple has its own API. 
# httpe://itunes.apple.com/search?entity=song&limit=1&term=weezer 
# here the search function tells us what we are donig at this url
# entity = song i.e. what we are searching for
# limit = the amount of songs we are searching for
# term = weezer i.e. context of the song. 
# you can find this data in the documentation. 

import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

    # lets write some python code to pretend to be a browser:
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

# produce a dictionary

# lets format this output. 
# using the json library that helps us read this more clearly. 
# using the dumps() we can create a dicitonary i.e. a curly bracket funciton - more keys more values. 

# lets grab all the songs they have access too:

o = response.json()
for result in o["results"]:
    print(result["trackName"])
