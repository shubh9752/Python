

a=str(input("enter your name "))
if a[0].isupper():
    print(1)
elif a[0].islower():
    print(-1)
else:
    print("not a valid name")