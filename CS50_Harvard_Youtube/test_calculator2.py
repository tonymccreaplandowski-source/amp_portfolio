from calculator import square # what we're testing

def test_positive():
    assert square(2) == 4
    assert square(3) == 9 # first assertion is failing.
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
def test_zero():
    assert square(0) == 0 

# we can also test for the correct data type i.e. int vs str
def test_str():
    with pytest.raises(TypeError):
        square("cat")

# no main function
# no trys 
# no conditionals 
# pytest won't tell you WHY your test failed or HOW to fix it - but it gives you a clue. 
# really helpful to break your code into bitsized funcitons such that we can test each one individually. 
# generally speaking your tests should be simple. 
# but the more code we can see which fails, the more clues to the ficture we can get. 
# lets break the test apart into catageries. 
# "FF.  = fail, fail, pass."
# doens't mean your code is perfect but that it passed your tests .
