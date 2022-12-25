print("welcome to bmi checker")
height=float(input("enter your height in m "))
weight=int(input("enter your weight in kg "))
bmi=weight/(height**2/10)
print("your bmi is ",round(bmi))
if bmi<=18.5:
    print("you are under weight")
elif bmi>18.5 and bmi<=25:
    print("you have normal weight")
elif bmi>25 and bmi<=30:
    print("do excercise you are over weight")
elif bmi>30 and bmi<35:
    print("find gym fatty")
else:
    print("find doctor")