import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students_2.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames = ["name", "home"])
    writer.writerow([name, home])

# with dictwriter we can pass ANY order of names and it will grab in whichever pair key is given
# as opposed to CSV which requires the lines are consistent.   