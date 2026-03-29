# program specific program designed to test calculator.py 

from calculator import square

# kick off the process:
def main():
    test_square()

# convention to call the funciton to test the funciton, "test_functionname()"
def test_square():
    try:
        assert square(2) == 4 # instead of saying something ins't true !=
    except AssertionError:
        print("2 squared was not 4")
        assert square(3) == 9  
    except AssertionError:
        print("3 squared was not 9")
        assert square(-2) == 4  
    except AssertionError:
        print("-2 squared was not 9")
        assert square(-3) == 9  
    except AssertionError:
        print("-3 squared was not 9")        
        assert square(0) == 0  
    except AssertionError:
        print("3 squared was not 9")

if __name__ == "__main__":
    main()

# note in this case only the second will fail because coinsidentally, 2+2 = 2*2 
# but here we wrote more code testing the code then the actual function.
# so we are going to shorten this -> using assert. 
# half as much code just to tell us we get an  "AssertionError"

