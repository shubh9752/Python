import random

num=int(input("enter the seed number "))
random.seed(num)

coin_side=random.randint(0,1)
if coin_side==1:
    print("tails")
else:
    print("heads")