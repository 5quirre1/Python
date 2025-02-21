import calendar

def search(year, month):
    if not (1 <= month <= 12):
        print("Error: there's 12 months dummy")
        return
    if year > 2100:
        print("Error: too far into future. Do a number UNDER 2100.")
        return
    
    print("\n" + calendar.month(year, month))

def main():
    try:
        year = int(input("Enter the year (e.g., 2025): "))
        month = int(input("Enter the month (1-12): "))
        search(year, month)
    except ValueError:
        print("error: use numbers plz")

if __name__ == "__main__":
    main()
