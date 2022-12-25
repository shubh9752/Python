print("average age of human being is 90 years \n lets check how much years,days,maonth and week you left!")
age=int(input("enter your age"))
years_left=90-age
days_left=years_left*365
week_left=years_left*52
month_left=years_left*12
print(f"you have {years_left} years,{month_left} month,{week_left} weeks and {days_left} days left")