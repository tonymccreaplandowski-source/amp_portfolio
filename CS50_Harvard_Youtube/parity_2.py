# 
def main():
    x = int(input("What's X? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd fn")

def is_even(n):
    """
    if n % 2 == 0:
        return True
    else:
        return False
    """
    """
    # shorter still
        return True if n % 2 == 0 else False #boolen 
    """
# shorter still
    return n % 2 == 0 

main() #in this current state this would break because is_even is undefined. So we define is_even BEFORE calling main.