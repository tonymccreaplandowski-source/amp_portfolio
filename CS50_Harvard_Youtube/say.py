import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1]) #concatenate the other argument. 

    # can be a cow
    # can be trex 
