year = int(input("What is the current year? "))
your_year = int(input("Enter your birth year: "))

if your_year > year or your_year < 1904:
    print("Incorrect Year")
elif your_year == year:
    print("0")
elif your_year < year or your_year > 1904:
    print(year - your_year)
    print("Years")