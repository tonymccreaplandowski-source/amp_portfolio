def main():
    x = int(input("What's x?" ))
    print("x squared is", square(x))

def square(n):
    return n * n #change this to test breaking your code. 

# ensures main is not called itself 
if __name__ == "__main__":
    main() 

# now lets test representative corner cases

