year=int(input("enter year you want to find"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year, " it's a leap year")
        else:
            print(year, " no it,s not a leap year")
    else:
        print(year," is leap year")
else:
    print(f"{year} is not a leap year")