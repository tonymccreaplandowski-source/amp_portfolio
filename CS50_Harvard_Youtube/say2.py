import sys

from saying import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])

# blindly calling main() at the end of saying.py the main() funciton WILL get called as well 
# this is why at the end of this program you will see hello world and goodbye world as well as the cow. 
# main gets called either way.
# the proper method ot call main is to NOT unconditionally call main.

# in saying add the following:
"""
if __name__ = "__main__":
    main()
"""
