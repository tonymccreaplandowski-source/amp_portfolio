score = int(input("Score: "))
#emplicitely knowing that if its NOT greater than 90 but greater than 80 then we can shorten the code 
if score >= 90: 
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")