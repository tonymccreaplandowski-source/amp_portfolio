import random

print(" // Challenge 1 // ")

# we are calling the specific funciton AND its module. 
coin = random.choice(["heads", "tails"])
print(coin)

# say we want to remove the need to having to call "random" module again and again
from random import choice # here we are calling the function explicitly 
# you might want to do this in case you were using the same module / function names and keep everything separate. 
# we can call choice and make this easier. 

print(" // Challenge 2 // ")

# USING random.randint(a, b):
import random

number = random.randint(1, 10)
print(number)

print(" // Challenge 3 // ")

# using random.shuffle(x): 

cards = ["jack", "queen", "king"]
random.shuffle(cards) #shuffle the list its given. \
for card in cards:
    print(card) # prints one at a time. 

print(" // Challenge 4 // ")

import statistics

#average 
print(statistics.mean([100, 90]))

print(" // Challenge 4 // ")
