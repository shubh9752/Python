print("welcome to python pizza delivery service")
pizza=input("enter your pizza size ? in 's','m' and 'l': ")
pepproni=input("want extra pepporoni? 'y' and 'n' :")
cheese=input("want extra cheese? 'y' and 'n' :")
s=15
m=20
l=25
if pizza=="s":
    if pepproni=="y":
        if cheese=="y":
            print("your bill is of amount ",s+2+1)
        else:
            print("your bill  is of amount ",s+2)
    else:
        print("your bill is of amount ",s)
elif pizza=="m":
    if pepproni=="y":
        if cheese=="y":
            print("your bill is of amount ",m+3+1)
        else:
            print("your bill  is of amount ",m+3)
    else:
        print("your bill is of amount ",m)
elif pizza=="l":
    if pepproni=="y":
        if cheese=="y":
            print("your bill is of amount ",l+3+1)
        else:
            print("your bill  is of amount ",l+3)
    else:
        print("your bill is of amount ",l)
else:
    print("please choose a valid option")