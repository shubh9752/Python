print("lets calculate the tip for good service of waiter")
bill=float(input("enter total bill amount? Rs."))
split_into=int(input("how many person you are "))
tip_percentage=int(input("enter the amount in percentage for a tip to give: "))
waiter_tip=(float(bill/100)*tip_percentage)
total_amount=waiter_tip+bill
on_each=total_amount/split_into
bill_split=bill/split_into
print(on_each,f"waitor tip rs{waiter_tip} and bill have to pay {bill_split}")