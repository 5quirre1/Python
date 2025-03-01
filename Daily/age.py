import time as greg
from datetime import *

def main():
    print("Welcome to age finder or something")
    greg.sleep(1)
    print("anyway..")
    greg.sleep(1)
    print("Choose an option:\n1: Your age this year\n2: Your age in a specific year")
    option = input(">> ")
    match option:
        case "1":
            currentYearAge()
        case "2":
            specificYearAge()
    

def specificYearAge():
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    day = int(input("Enter a day: "))

    byear = int(input("Enter your birth year: "))
    bmonth = int(input("Enter your birth month: "))
    bday = int(input("Enter your birth day: "))

    if (month < 1 or month > 12) or (day < 1 or day > 31):
        print("Invalid date")
        return
    if (bmonth < 1 or bmonth > 12) or (bday < 1 or bday > 31):
        print("Invalid birth date")
        return

    input_date = datetime(year, month, day)
    birth_date = datetime(byear, bmonth, bday)
    age = input_date.year - birth_date.year - ((input_date.month, input_date.day) < (birth_date.month, birth_date.day))

    greg.sleep(1)
    print(f"You are {age} years old on {input_date.strftime('%m/%d/%Y')}")
def currentYearAge():
    year = int(input("Enter your birth year: "))
    month = int(input("Enter your birth month: "))
    day = int(input("Enter your birth day: "))
    
    if month > 12 or day > 31:
        print("Invalid date")
        return
    elif month < 1 or day < 1:
        print("Invalid date")
        return

    current_year = date.today().year
    age = current_year - year
    greg.sleep(1)
    print(f"You are {age} years old")
    


if __name__ == "__main__":
    main()
    
