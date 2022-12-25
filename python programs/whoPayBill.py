import random
print("lets play who pay the bill")
num=int(input("enter a random number"))
random.seed(num)
names=input("enter peoples name, seperated by coma eg.shubham, ritu")
names_list=names.split(",")
last_index=len(names_list)
random_name=random.randint(0,last_index-1)

print(names_list[random_name])