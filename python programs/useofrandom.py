import random

#choosing random integer
#it will give random number from 0-99 including 0-99
num=random.randint(0,99)
print(num)
num1=random.randint(-10,10)
print(num1)

#choosing float random
#it will give rondom float b/t given number but not include them
#float random value dont takes argument ..it will auto set to 0.0-1.0
#you can choose betbeen float num by multiplying them them
num2=random.random()
print(round(num2))
num3=random.random()*7
print(num3)
